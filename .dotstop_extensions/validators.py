from typing import TypeAlias
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
    if github_event_name != "pull_request" and "dependency_review" in configuration:
        configuration["dependency_review"] = "exclude"  # Exclude dependency review if not a PR

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
