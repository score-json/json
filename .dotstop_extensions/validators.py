from typing import TypeAlias, Tuple, List
import os
import requests
import sqlite3
import sys

current_dir = os.getcwd()
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from TSF.scripts.generate_list_of_tests import ListOfTestsGenerator
import hashlib
import json
import re
import subprocess

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
    raw_tests = configuration.get("tests",None)
    if raw_tests is None:
        return(1.0, [Warning("Warning: No tests specified! Assuming absolute trustability!")])
    # process test-names
    tests = []
    for test in raw_tests:
        tests.append(f"test-{str(test)}")
    # read optional argument -- database name for the test report -- if specified
    database = configuration.get("database", None)
    if database is None:
        # default value "MemoryEfficientTestResults.db"
        database = "MemoryEfficientTestResults.db"
    # check whether database containing test-results does exist
    ubuntu_artifact = f"./artifacts/{database}"
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
        if cursor.fetchone() is None:
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
    
def check_list_of_tests(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    # initialise the generator
    generator = ListOfTestsGenerator()
    db = configuration.get("database",None)
    if db is not None:
        generator.set_database(db)
    table = configuration.get("table",None)
    if table is not None:
        generator.set_table(table)
    sources = configuration.get("sources",None)
    if sources is not None:
        generator.set_sources(sources)
    
    # fetch the expected result
    try:
        with open("./TSF/docs/list_of_test_environments.md", 'r') as f:
            expected = f.read()
            if expected == generator.fetch_all_test_data():
                return(1.0,[])
            else:
                return(0.0,[Exception("The expected list of test-cases does not coincide with the fetched list.")])
    except:
        return(0.0,[Exception("An exception occurred when trying to compare the expected and the fetched list of tests.")])

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
        my_sha = hashlib.sha256(open(file,"rb").read()).hexdigest()
        score = 1.0 if str(my_sha) == expected_sha else 0.0
    except:
        exceptions.append(RuntimeError(f"Can't calculate the SHA-value of {file}"))
    return (score, exceptions)

def check_issues(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    from datetime import datetime, timezone
    # get relevant release date
    release_date = configuration.get("release_date",None)
    if release_date is None:
        return (0.0, [RuntimeError("The release date of the most recent version of nlohmann/json is not specified.")])
    else:
        try:
            release_time = datetime.strptime(release_date,"%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()
        except:
            return(0.0, [RuntimeError("The format of the release date is to be %Y-%m-%dT%H:%M:%SZ")])
    # get path to static list of misbehaviours
    raw_known_misbehaviours = configuration.get("list_of_known_misbehaviours",None)
    # parse list of inapplicable misbehaviours
    inapplicable_misbehaviours = []
    if raw_known_misbehaviours is not None:
        try:
            # open the list of known misbehaviours
            with open(raw_known_misbehaviours) as f:
                lines = f.readlines()
        except:
            # if list can not be opened, assume that there is no list
            lines = []
        # parse list of known misbehaviours
        for line in lines:
            entries = line.split('|')
            try:
                id = int(entries[0])
            except ValueError:
                continue
            if len(entries)>1 and entries[1].strip().upper()=="NO":
                inapplicable_misbehaviours.append(id)
    # parse raw list of open misbehaviours
    try:
        with open("raw_open_issues.json") as list_1:
            all_open_issues = json.load(list_1)
        relevant_open_issues = [all_open_issues[i].get("number",None) 
                                    for i in range(0,len(all_open_issues))
                                        if len(all_open_issues[i].get("labels",[]))!=0 
                                        and (all_open_issues[i].get("labels"))[0].get("name") == "kind: bug"
                                ]
    except:
        return(0.0, [RuntimeError("The list of open issues could not be extracted.")])
    for issue in relevant_open_issues:
        if issue not in inapplicable_misbehaviours and issue is not None:
            return(0.0, [])  
    # parse raw list of closed misbehaviours
    try:
        with open("raw_closed_issues.json") as list_2:
            all_closed_issues = json.load(list_2)
        relevant_closed_issues = [all_closed_issues[i].get("number",None) 
                                    for i in range(0,len(all_closed_issues))
                                        if len(all_closed_issues[i].get("labels",[]))!=0 
                                        and (all_closed_issues[i].get("labels"))[0].get("name") == "kind: bug"
                                        and datetime.strptime(all_closed_issues[i].get("createdAt","2000-01-01T00:00:00Z"),"%Y-%m-%dT%H:%M:%SZ")
                                                                                  .replace(tzinfo=timezone.utc)
                                                                                  .timestamp()
                                            >=release_time
                                ]
    except:
        return(0.0, [RuntimeError("The list of closed issues could not be extracted.")])
    for issue in relevant_closed_issues:
        if issue not in inapplicable_misbehaviours and issue is not None:
            return(0.0, [])  
    # If you are here, then there are no applicable misbehaviours.
    return (1.0, [])

def did_workflows_fail(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    owner = configuration.get("owner",None)
    if owner is None:
        return (0.0, [RuntimeError("The owner is not specified in the configuration of did_workflows_fail.")])
    repo = configuration.get("repo",None)
    if repo is None:
        return (0.0, [RuntimeError("The repository is not specified in the configuration of did_workflows_fail.")])
    event = configuration.get("event","push")
    url = f"https://github.com/{owner}/{repo}/actions?query=event%3A{event}+is%3Afailure"
    branch = configuration.get("branch",None)
    if branch is not None:
        url += f"+branch%3A{branch}"
    
    try:
        res = requests.get(url, timeout=30)  # Add timeout to prevent hanging
    except requests.exceptions.ConnectionError as e:
        return (0.0, [RuntimeError(f"Connection error when accessing {url}: {e}")])
    except requests.exceptions.Timeout as e:
        return (0.0, [RuntimeError(f"Timeout error when accessing {url}: {e}")])
    except requests.exceptions.RequestException as e:
        return (0.0, [RuntimeError(f"Request error when accessing {url}: {e}")])
    
    if res.status_code != 200:
        return (0.0, [RuntimeError(f"The website {url} can not be successfully reached! Status code: {res.status_code}")])
    m = re.search(r'(\d+)\s+workflow run results', res.text, flags=re.I)
    if m is None:
        return (0.0, [RuntimeError("The number of failed workflows can not be found.")])
    if m.group(1).strip() != "0":
        return (0.0, [Warning("There are failed workflows!")])
    return (1.0, [])
    
def coveralls_reporter(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    owner = configuration.get("owner",None)
    if owner is None:
        return (0.0, [ValueError("The owner needs to be specified in the configuration for coveralls_reporter.")])
    repo = configuration.get("repo",None)
    if repo is None:
        return (0.0, [ValueError("The repository needs to be specified in the configuration for coveralls_reporter.")])
    branch = configuration.get("branch",None)
    if branch is not None:
        url = f"coveralls.io/github/{owner}/{repo}?branch={branch}.json"
    else:
        url = f"coveralls.io/github/{owner}/{repo}.json"
    res = requests.get(url)
    if res.status_code != 200:
        return (0.0, [RuntimeError(f"Can not reach {url} to fetch the code coverage!")])
    res = json.loads(res.text)
    try:
        covered_lines = int(res.get("covered_lines","0"))
        relevant_lines = int(res.get("relevant_lines","1"))
    except ValueError:
        return (0.0, [RuntimeError("Critical error in the coveralls api: Expecting integer values for lines!")])
    try:
        expected_line_coverage = float(configuration.get("line_coverage","0.0"))
    except ValueError:
        return (0.0, [ValueError("line_coverage needs to be a floating point value!")])
    try:
        digits = int(configuration.get("significant_decimal_digits","3"))
    except ValueError:
        return (0.0, [ValueError("significant_decimal_digits needs to be an integer value!")])
    if round(expected_line_coverage, digits) != round(covered_lines/relevant_lines * 100, digits):
        return (0.0, [Warning("The line coverage has changed!")])
    try:
        covered_branches = int(res.get("covered_branches","0"))
        relevant_branches = int(res.get("relevant_branches","1"))
    except ValueError:
        return (0.0, [RuntimeError("Critical error in the coveralls api: Expecting integer values for branches!")])
    try:
        expected_branch_coverage = float(configuration.get("branch_coverage","0.0"))
    except ValueError:
        return (0.0, [ValueError("branch_coverage needs to be a floating point value!")])
    if round(expected_branch_coverage, digits) != round(covered_branches/relevant_branches * 100, digits):
        return (0.0, [Warning("The branch coverage has changed!")])
    return (1.0, [])
    


def combinator(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    validators = configuration.get("validators",None)
    if validators is None:
        return (1.0, [Warning("No validators were given, returning the void-validator.")])
    elif not isinstance(validators,list):
        return (0.0, [TypeError("The list of validators must be given as list.")])
    scores = []
    exceptions = []
    weights = []
    for validator in validators:
        # fetch configuration
        validator_configuration = validator.get("configuration", None)
        if not isinstance(validator_configuration,dict[str, yaml]):
            return (0.0, [TypeError("Validator configuration must be an object.")])
        # fetch weight
        weight = float(validator.get("weight",1.0))
        if weight<0:
            return (0.0, [TypeError("Validator weights must be non-negative.")])
        weights.append(weight)
        # fetch type
        validator_type = validator.get("type", None)
        if validator_type is None:
            return (0.0, [TypeError("Missing validator type declaration.")])
        # execute validator
        if validator_type == "check_artifact_exists":
            validator_score, validator_errors = check_artifact_exists(validator_configuration)
            scores.append(validator_score)
            exceptions.extend(validator_errors)
        elif validator_type == "https_response_time":
            validator_score, validator_errors = https_response_time(validator_configuration)
            scores.append(validator_score)
            exceptions.extend(validator_errors)
        elif validator_type == "check_test_results":
            validator_score, validator_errors = check_test_results(validator_configuration)
            scores.append(validator_score)
            exceptions.extend(validator_errors)
        elif validator_type == "file_exists":
            validator_score, validator_errors = file_exists(validator_configuration)
            scores.append(validator_score)
            exceptions.extend(validator_errors)
        elif validator_type == "sha_checker":
            validator_score, validator_errors = sha_checker(validator_configuration)
            scores.append(validator_score)
            exceptions.extend(validator_errors)
        elif validator_type == "check_issues":
            validator_score, validator_errors = check_issues(validator_configuration)
            scores.append(validator_score)
            exceptions.extend(validator_errors)
        elif validator_type == "did_workflows_fail":
            validator_score, validator_errors = did_workflows_fail(validator_configuration)
            scores.append(validator_score)
            exceptions.extend(validator_errors)
        elif validator_type == "coveralls_reporter":
            validator_score, validator_errors = coveralls_reporter(validator_configuration)
            scores.append(validator_score)
            exceptions.extend(validator_errors)
    if sum(weights) == 0.0:
        return (0.0, exceptions)
    else:
        return (sum(list(map(lambda x,y: x*y, scores, weights)))/sum(weights),exceptions)
