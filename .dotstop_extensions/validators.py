from typing import TypeAlias, tuple, list
import os
import requests

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
    env = setup_environment_variables()
    
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


