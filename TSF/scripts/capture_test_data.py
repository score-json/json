import sys
import sqlite3
import os
import xml.etree.ElementTree as ET
import re
from datetime import datetime

def setup_environment_variables() -> dict[str, str]:
    """
    Retrieves and validates the necessary environment variables for GitHub workflows.
    Raises a RuntimeError if any required variables are missing.
    """
    required_vars = ["GITHUB_RUN_ID", "GITHUB_REPOSITORY", "GITHUB_RUN_ATTEMPT"]
    environment = {var: os.getenv(var) for var in required_vars}
    
    missing_vars = [var for var, value in environment.items() if not value]
    if missing_vars:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    return environment

def clean_test_case(testcase: str) -> tuple[str,str]:
    """
    This function expects a testcase of the form "testcase_name_cppxx".
    It returns the tuple ["testcase_name","gnu++xx"].
    """
    name, appendix = testcase.rsplit('_',1)
    return [name, "gnu++"+appendix.replace('cpp','')]

def read_result_table(input: list[str]) -> dict:
    """
    This function expects console output <system-out> of doctest.
    It is assumed that this has the following form
        <system-out>[doctest] doctest version is "2.4.11"
        [doctest] run with "--help" for options
        ===============================================================================
        [doctest] test cases:  1 |  1 passed | 0 failed | 0 skipped
        [doctest] assertions: 45 | 45 passed | 0 failed |
        [doctest] Status: SUCCESS!
        </system-out>
    It extracts the number of passed/failed/skipped test cases, and passed/skipped assertions.
    """
    metadata = dict()
    raw_data = next(input)
    data = re.findall(r'(\d+)\s+(passed|failed|skipped)\b', raw_data)
    metadata["passed test cases"] = int(data[0][0])
    metadata["failed test cases"] = int(data[1][0])
    metadata["skipped test cases"] = int(data[2][0])
    metadata["passed assertions"] = int(data[3][0])
    metadata["failed assertions"] = int(data[4][0])
    return metadata


def get_metadata(testcase: ET.Element) -> dict:
    """
    This function expects a testcase extracted from a junit xml-file as input
    """
    metadata = dict()
    unsplit_name = testcase.get("name")
    name, standard = clean_test_case(unsplit_name)
    metadata["name"] = name
    metadata["standard"] = standard
    metadata["execution time"] = float(testcase.get("time"))
    metadata = metadata | read_result_table(testcase.find("system-out").itertext())
    return metadata

def is_unit_test(testcase: ET.Element) -> bool:
    return "_cpp" in testcase.get('name')

def get_all_xml_files(directory: str = '.') -> list[str]:
    result = []
    content = os.listdir(directory)
    for entry in content:
        if os.path.isdir(directory+'/'+entry):
            result = result + get_all_xml_files(directory+'/'+entry)
        if entry.endswith('.xml'):
            file = directory+'/'+entry if directory != '.' else entry
            result.append(file)
    return result

# get environment variables
try:
    environment = setup_environment_variables()
except RuntimeError as e:
    raise RuntimeError("Critical error: Can not uniquely identify environment data! Aborting recording of data.")

# initiate connection to database
connector = sqlite3.connect("TSF/TestResultData.db")
connector.execute("PRAGMA foreign_keys = ON")
cursor = connector.cursor()

# load expected tables
command = (
    "CREATE TABLE IF NOT EXISTS workflow_info(",
    "repo TEXT, ",                              # repository
    "run_id INT, ",                             # ID of workflow run
    "run_attempt INT, ",                        # Attempt-number of workflow run
    "status TEXT ",                              # Termination-status of workflow
    "CHECK(status IN ('successful', 'failed', 'cancelled')) DEFAULT 'failed', ",
    "PRIMARY KEY(repo, run_id, run_attempt))"
)
cursor.execute(''.join(command))
command = (
    "CREATE TABLE IF NOT EXISTS test_results(",
    "timestamp INT, "                           # when the test-run was started
    "name TEXT, ",                              # name of the test
    "execution_time REAL, ",                    # execution time in seconds
    "compiler TEXT, ",                          # compiler information
    "cpp_standard TEXT, ",                      # cpp-standard
    "passed_cases INT, ",                       # number of passed test-cases
    "failed_cases INT, ",                       # number of failed test-cases
    "skipped_cases INT, ",                      # number if skipped test-cases
    "passed_assertions INT, ",                  # number of passed assertions
    "failed_assertions INT, ",                  # number of failed assertions
    "repo TEXT, ",                              # repository
    "run_id INT, ",                             # ID of workflow run
    "run_attempt INT, ",                        # Attempt-number of workflow run
    "FOREIGN KEY(repo, run_id, run_attempt) REFERENCES workflow_info)"
    )
cursor.execute(''.join(command))

# fill in metadata
# BEACHTE: This script expects the status of the github workflow as argument
repo = environment.get('GITHUB_REPOSITORY')
run_id = environment.get('GITHUB_RUN_ID')
run_attempt = environment.get('GITHUB_RUN_ATTEMPT')
command = f"INSERT INTO workflow_info VALUES('{repo}', {run_id}, {run_attempt}, '{sys.argv[1]}')"
cursor.execute(command)
# Don't forget to save!
connector.commit()

# Load my artifacts
failed_data = []
junit_logs = get_all_xml_files("./my_artifacts/")

#extract data
for junit_log in junit_logs:
    tree = ET.parse(junit_log)
    file_root = tree.getroot()
    testsuite = next(file_root.iter('testsuite'), None)
    if testsuite is None:
        print(f"Error: Could not find testsuite data in {junit_log}.")
        failed_data.append(junit_log)
        continue
    for testcase in (case for case in file_root.iter('testcase') if is_unit_test(case)):
        metadata = get_metadata(testcase)
        command = (
            "INSERT INTO test_results VALUES(",
            f"{int(datetime.fromisoformat(testsuite.get('timestamp')).timestamp())}, ",
            f"'{metadata.get('name')}', ",
            f"{metadata.get('execution time')}, ",
            f"'{testsuite.get('name')}', ",
            f"'{metadata.get('standard')}', ",
            f"{metadata.get('passed test cases')}, ",
            f"{metadata.get('failed test cases')}, ",
            f"{metadata.get('skipped test cases')}, ",
            f"{metadata.get('passed assertions')}, ",
            f"{metadata.get('failed assertions')}, ",
            f"'{repo}', ",
            f"{run_id}, ",
            f"{run_attempt}"
            ")"
        )
        command = "".join(command)
        cursor.execute(command)
        connector.commit()

conn = sqlite3.connect("TestResults.db")
cur = conn.cursor()
command = (
    "CREATE TABLE IF NOT EXISTS test_results(",
    "name TEXT, ",                              # name of the test
    "execution_time REAL, ",                    # execution time in seconds
    "compiler TEXT, ",                          # compiler information
    "cpp_standard TEXT, ",                      # cpp-standard
    "passed_cases INT, ",                       # number of passed test-cases
    "failed_cases INT, ",                       # number of failed test-cases
    "skipped_cases INT, ",                      # number if skipped test-cases
    "passed_assertions INT, ",                  # number of passed assertions
    "failed_assertions INT",                  # number of failed assertions
    ")"
    )
cur.execute(''.join(command))
cur.execute("ATTACH DATABASE 'TSF/TestResultData.db' AS source")
command = (
    "INSERT INTO test_results (name, execution_time, compiler, cpp_standard, passed_cases, failed_cases, skipped_cases, passed_assertions, failed_assertions)",
    "SELECT name, execution_time, compiler, cpp_standard, passed_cases, failed_cases, skipped_cases, passed_assertions, failed_assertions",
    "FROM source.test_results WHERE"
    f"repo = '{repo}' AND"
    f"run_id = {run_id} AND"
    f"run_attempt = {run_attempt})"
)
cur.execute(''.join(command))
conn.commit()
conn.close()

# terminate connection to database
connector.commit() # save, for good measure
connector.close()
