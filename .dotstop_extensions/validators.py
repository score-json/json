from typing import TypeAlias, Tuple, List
import os
import requests
import sqlite3
import hashlib

yaml: TypeAlias = str | int | float | list["yaml"] | dict[str, "yaml"]

def setup_environment_variables() -> dict[str, str]:
    """
    Retrieves and validates the necessary environment variables for GitHub workflows.
    Raises a RuntimeError if any required variables are missing.
    """
    required_vars = ["GITHUB_TOKEN", "GITHUB_EVENT_NAME", "GITHUB_RUN_ID", "GITHUB_REPOSITORY", "GITHUB_SHA"]
    environment = {var: os.getenv(var) for var in required_vars}
    
    missing_vars = [var for var, value in environment.items() if not value]
    if missing_vars:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    return environment

def check_artifact_exists(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:    
    # Setup environment variables using the helper function
    try:
        env = setup_environment_variables()
    except RuntimeError as e:
        return (0,[e])
    
    github_token = env["GITHUB_TOKEN"]
    github_event_name = env["GITHUB_EVENT_NAME"]
    run_id = env["GITHUB_RUN_ID"]
    repository = env["GITHUB_REPOSITORY"]
    sha = env["GITHUB_SHA"]
    
    score = 0.0

    # Validate configuration values
    for key, value in configuration.items():
        if value not in {"include", "exclude"}:  # Check if value is valid
            warning = Warning(f"Invalid configuration value: '{value}' for key '{key}'. Valid values are 'include' or 'exclude'.")
            return (0.0, [warning]) # If value is neither include nor exclude, return 0.0 with a warning

    # Determine the number of expected workflows based on the event type
    if github_event_name != "pull_request":
        configuration["dependency_review"] = "exclude"  # Exclude dependency review if not a PR
        configuration["check_amalgamation"] = "exclude"  # Exclude check amalgamation if not a PR

    if github_event_name != "push":
        configuration["publish_documentation"] = "exclude"  # Exclude publish documentation if not a push to main

    num_expected_workflows = sum(1 for value in configuration.values() if value == "include")

    # If no workflows are expected, return a score of 1.0 with a warning
    if num_expected_workflows == 0:
        warning = Warning("No workflows to check, returning a score of 1.0.")
        return (1.0, [warning])

    # GitHub API URL to list artifacts for the current workflow run
    url = f"https://api.github.com/repos/{repository}/actions/runs/{run_id}/artifacts"

    # Add authentication headers using the GitHub token
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json"
    }

    # Make the request to the GitHub API to fetch artifacts
    response = requests.get(url, headers=headers)

    # Check for a successful response
    if response.status_code != 200:
        return (score, [RuntimeError(f"Failed to fetch artifacts: {response.status_code} - {response.text}")])

    # Parse the JSON response
    data = response.json()
    artifacts_created_data = data.get("artifacts", [])

    # Extract artifact names
    artifacts_created = [artifact["name"] for artifact in artifacts_created_data]

    # Check if artifacts for each workflow exist    
    for key, value in configuration.items():
        if value == "exclude":
            continue  # Skip excluded workflows
        artifact_expected = f"{key}-{sha}"
        if artifact_expected in artifacts_created:
            score += 1

    return (score/num_expected_workflows, [])


def https_response_time(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    """
    Validates the reachability of a website-reference.
    This code is mostly copied from https://codethinklabs.gitlab.io/trustable/trustable/trudag/validators.html,
    where this custom validator is presented as an example.

    notable difference: target response time is given in seconds, since we only check if the website is reachable.
    """
    target = configuration.get("target_seconds", None)
    urls = configuration.get("urls", None)
    if not urls:
        return (0.0, [ValueError("No url specified for https_response_time validator")])
    if not target:
        return (0.0, [ValueError("No target time specified for https_response_time validator")])
    exceptions = []
    scores = []
    for url in urls:
        try:
            # in the reference website, an url comes together with https://
            response = requests.get(url,timeout=5*target)
        except requests.exceptions.ConnectionError as e:
            print(f"Critical error: target site {url} could not be reached.")
            exceptions.append(e)
            scores.append(0)
            continue
        except requests.exceptions.ReadTimeout as e:
            print(f"Error: target site {url} could not be reached within {5*target} seconds.")
            exceptions.append(e)
            scores.append(0)
            continue
        # check whether target site is successfully called
        if response.status_code == 200:
            # if target site is successfully called, check if it is reached within target seconds
            # recall that target/response.elapsed.microseconds>1/5, so score is accordingly refactored 
            score = (min(1e6*target/response.elapsed.microseconds, 1.0)-0.2)*1.25
            scores.append(score)
            continue
        scores.append(0)
    return(sum(scores)/len(scores),exceptions)


def check_test_results(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    """
    Validates whether a certain test-case fails, or not.
    """
    # get the test-names
    tests = configuration.get("tests",None)
    if tests is None:
        return(1.0, Warning("Warning: No tests specified! Assuming absolute trustability!"))
    # check whether the most recent test report is loaded
    sha = os.getenv("GITHUB_SHA")
    if not sha:
        return (0.0, [RuntimeError("Can't get value GITHUB_SHA.")])
    ubuntu_artifact = f"./artifacts/ubuntu-{str(sha)}"
    # check whether ubuntu-artifact is loaded correctly
    if not os.path.exists(ubuntu_artifact):
        return (0.0, [RuntimeError("The artifact containing the test data was not loaded correctly.")])
    # read optional argument -- database name for the test report -- if specified
    database = configuration.get("database", None)
    if database is None:
        # default value "MemoryEfficientTestResults.db"
        database = "MemoryEfficientTestResults.db"
    # check whether database containing test-results does exist
    ubuntu_artifact += "/"+database
    if not os.path.exists(ubuntu_artifact):
        return (0.0, [RuntimeError("The artifact containing the test data was not loaded correctly.")])
    # Ubuntu artifact is loaded correctly and test-results can be accessed.
    # read optional argument -- table name for the test report -- if specified
    table = configuration.get("table", None)
    if table is None:
        # default value "test_results"
        table = "test_results"
    # establish connection to database
    try:
        connector = sqlite3.connect(ubuntu_artifact)
        cursor = connector.cursor()
        # check whether our results can be accessed
        cursor.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,))
        if not cursor.fetchone():
            # if not, it is not trustable
            return (0.0, [RuntimeError(f"Table {table} can not be loaded.")])
        # our result table can be read
        # initialise variables 
        score = 0.0
        expected_tests = len(tests)
        warnings = []
        for test in tests:
            # check if data for test have been captured
            command = f"SELECT COUNT(*) FROM {table} WHERE name = ?"
            cnt = cursor.execute(command, (test)).fetchone()[0]
            if cnt is None or cnt == 0:
                # no data found -> assign trustability 0 and inform user
                warnings.append(Warning(f"Could not find data for test {test}."))
                continue
            # process data for test
            command = f"""
                        SELECT
                            COALESCE(SUM(passed_cases), 0) AS total_passed,
                            COALESCE(SUM(failed_cases), 0) AS total_failed
                        FROM {table}
                        WHERE name = ?
                    """
            passed, failed = cursor.execute(command, (test,)).fetchone()
            all = float(passed)+float(failed)
            if all == 0:
                # means that all test-cases have been skipped; could happen due to time-constraints
                # and interrupted workflow.
                # Assumption: A skipped test is trustable.
                score += 1/expected_tests
                warnings.append(Warning(f"All test cases of {test} were skipped."))
            else:
                # at least one passed or failed test has been found
                # observe that expected_tests = 0 if, and only if, tests = [], 
                # in which case the for-loop is skipped
                score += float(passed)/(all*expected_tests)
        # terminate database connection 
        # no commit necessary, since changes on database not intended
        connector.close()
        return(score, warnings)
    except:
        return (0.0, [RuntimeError("Fatal error during database evaluation.")])    

def file_exists(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    # read list of files to be checked
    files = configuration.get("files",None)
    if files is None:
        return (1.0, [Warning("No files to check, assuming trustability")])
    expected_files = len(files)
    # if no files are to be checked, assume trustability
    if expected_files == 0:
        return (1.0, [Warning("No files to check, assuming trustability")])
    found_files = 0
    exceptions = []
    for file in files:
        # check if path exists
        if not os.path.exists(file):
            exceptions.append(RuntimeError(f"Critical Error: The path {file} does not exist."))
        elif os.path.isdir(file):
            # only files counted, warn user if directory is detected
            exceptions.append(Warning(f"The path {file} links to a directory, but a file is expected."))
        else:
            found_files += 1 if os.path.isfile(file) else 0
    return (found_files/expected_files, exceptions)

def sha_checker(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    # get file of which the sha is to be calculated
    file = configuration.get("binary", None)
    # test input on validitiy
    if file is None:
        return (1.0, [Warning("No files to check the SHA-value for; assuming that everything is in order.")])
    elif not isinstance(file, str):
        # type-errors are not tolerated
        raise TypeError("The value of \"binary\" must be a string")
    # get the expected sha
    expected_sha = configuration.get("sha", None)
    # test input on validitiy
    if expected_sha is None:
        return (1.0, [Warning("No expected SHA-value transmitted; assuming everything is in order.")])
    try: expected_sha = str(expected_sha) 
    except: raise TypeError("Can't convert the value of \"sha\" to a string.")
    score = 0.0
    exceptions = []
    try:
        my_sha = hashlib.sha256(open(file,"rb").read()).hexdigest
        score = 1.0 if str(my_sha) == expected_sha else 0.0
    except:
        exceptions.append(RuntimeError(f"Can't calculate the SHA-value of {file}"))
    return (score, exceptions)
