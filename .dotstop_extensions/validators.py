from typing import TypeAlias, Tuple, List
import os
import requests
import subprocess
import warnings

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

    # Determine the number of expected workflows based on the event type
    if github_event_name != "pull_request" and configuration.get("dependency_review") is not None:
        num_expected_workflows = len(configuration) - 1  # Exclude dependency review if not a PR
    else: 
        num_expected_workflows = len(configuration)

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
        raise RuntimeError(f"Failed to fetch artifacts: {response.status_code} - {response.text}")

    # Parse the JSON response
    data = response.json()
    artifacts = data.get("artifacts", [])

    # Extract artifact names
    artifact_names = [artifact["name"] for artifact in artifacts]
        
    # Check if artifacts for each workflow exist    
    for key, value in configuration.items():
        print(f"Checking workflow: {key},{value}")
        artifact_id = f"{value}-{sha}"

        if artifact_id in artifact_names:
            score += 1 / num_expected_workflows
            print(f"Artifact for workflow {key} found. Current cumulative score: {score}")
        else: 
            if str(value) == "dependency_review" and github_event_name != "pull_request":
                print(f"Skipped dependency_review workflow for non-PR.")
            else:
                print(f"Artifact for workflow {key} NOT found. Current cumulative score: {score}")

    return (score, [])

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
            score = (min(target/response.elapsed.microseconds, 1.0)-0.2)*1.25
            scores.append(score)
            continue
        scores.append(0)
    return(sum(scores)/len(scores),exceptions)   
