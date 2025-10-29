import sys
import sqlite3
import os
from datetime import datetime, timezone

def setup_environment_variables() -> dict[str, str]:
    # Retrieves and validates the necessary environment variables for GitHub workflows.
    # Raises a RuntimeError if any required variables are missing.
    required_vars = ["GITHUB_RUN_ID", "GITHUB_REPOSITORY", "GITHUB_RUN_ATTEMPT"]
    environment = {var: os.getenv(var) for var in required_vars}
    
    missing_vars = [var for var, value in environment.items() if not value]
    if missing_vars:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    return environment

def find_most_recent_cve_count(database: sqlite3.Connection) -> int:
    cursor = database.cursor()
    cursor.execute("""
                    SELECT total_count FROM cve_data
                    ORDER BY time DESC, run_id DESC, run_attempt DESC
                    LIMIT 1;
                    """)
    result = cursor.fetchone()
    return -1 if result is None else result[0]

##########################
# Below starts the script.
##########################

if __name__ == "__main__":

    # check if argument was delivered
    if len(sys.argv) != 2:
        raise RuntimeError("Expected CVE count as argument. Aborting!")
    
    # expected argument: total CVE count
    try:
        cve_count = int(sys.argv[1])
    except ValueError:
        raise RuntimeError("CVE count must be a valid integer. Aborting!")

    # get environment variables
    try:
        environment = setup_environment_variables()
    except RuntimeError as e:
        raise RuntimeError("Critical error: Can not uniquely identify environment data! Aborting recording of data.")
    
    # Step 1: store CVE data persistently

    # initiate connection to database
    connector = sqlite3.connect("TSF/MemoryEfficientTestResultData.db")
    connector.execute("PRAGMA foreign_keys = ON")

    # create CVE data table if it doesn't exist
    command = (
        "CREATE TABLE IF NOT EXISTS cve_data(",
        "total_count INT, ",                        # total number of open CVEs/security issues
        "repo TEXT, ",                              # repository
        "run_id INT, ",                             # ID of workflow run
        "run_attempt INT, ",                        # Attempt-number of workflow run
        "time INT, ",                               # the time that is associated to this workflow run
        "PRIMARY KEY(repo, run_id, run_attempt))"
    )
    connector.execute(''.join(command))
    cursor = connector.cursor()

    # Count number of rows as heuristic size-checker
    cursor.execute("SELECT COUNT(*) FROM cve_data;")
    if cursor.fetchone()[0] > 1000:  # Limit CVE data entries
        connector.close()
        raise RuntimeError("The CVE data storage is too large! Please clean up old entries.")

    # fill in CVE data
    repo = environment.get('GITHUB_REPOSITORY')
    run_id = environment.get('GITHUB_RUN_ID')
    run_attempt = environment.get('GITHUB_RUN_ATTEMPT')
    time = int(datetime.now(timezone.utc).timestamp())
    
    # Only store if the count has changed from the most recent entry
    most_recent_count = find_most_recent_cve_count(connector)
    if most_recent_count != cve_count:
        command = "INSERT INTO cve_data VALUES(?,?,?,?,?)"
        cursor.execute(command, (cve_count, repo, run_id, run_attempt, time))
        print(f"Stored new CVE count: {cve_count} (previous: {most_recent_count})")
    else:
        print(f"CVE count unchanged: {cve_count}, skipping storage")
    
    # Don't forget to save!
    connector.commit()
    connector.close()
    
    # Step 2: Create temporary database for artifact (similar to test results)
    
    # Initialize temporary database connection
    conn = sqlite3.connect("MemoryEfficientCVEResults.db")
    cur = conn.cursor()
    
    # Add the expected table for CVE data
    command = (
        "CREATE TABLE IF NOT EXISTS cve_data(",
        "total_count INT, ",                        # total number of open CVEs/security issues
        "time INT",                                 # timestamp
        ")"
    )
    conn.execute(''.join(command))
    
    # Insert current CVE data
    time = int(datetime.now(timezone.utc).timestamp())
    command = "INSERT INTO cve_data VALUES(?,?)"
    cur.execute(command, (cve_count, time))
    
    # Commit and close temporary database
    conn.commit()
    conn.close()
    
    print(f"CVE data capture completed. Total count: {cve_count}")
    print(f"Temporary database MemoryEfficientCVEResults.db created for artifact")