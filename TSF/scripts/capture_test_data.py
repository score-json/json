import sys
import sqlite3
import os
import xml.etree.ElementTree as ET
import re

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

def read_result_table(lines: list[str]) -> dict:
    """
    This function expects console output <system-out> of doctest.
    It extracts the number of passed/failed/skipped test cases, and passed/skipped assertions.
    """
    metadata = dict()
    for line in lines:
        if "test cases" in line:
            data = re.findall(r'(\d+)\s+(passed|failed|skipped)\b', line)
            metadata["passed test cases"] = int(data[0])
            metadata["failed test cases"] = int(data[1])
            metadata["skipped test cases"] = int(data[2])
            continue
        if "assertions" in line:
            data = re.findall(r'(\d+)\s+(passed|failed)\b', line)
            metadata["passed assertions"] = int(data[0])
            metadata["failed assertions"] = int(data[1])
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
    metadata = metadata | read_result_table(testcase.find("system-out"))
    return metadata

def is_unit_test(testcase: ET.Element) -> bool:
    return "_cpp" in testcase.get('name')

# get environment variables
try:
    environment = setup_environment_variables()
except RuntimeError as e:
    raise RuntimeError("Critical error: Can not uniquely identify environment data! Aborting recording of data.")

if os.path.exists("./my_artifacts"): print("Moin!")
for entry in os.listdir("./my_artifacts"):
    print(entry)

# # initiate connection to database
# connector = sqlite3.connect("TestResultData.db")
# connector.execute("PRAGMA foreign_keys = ON")
# cursor = connector.cursor()

# # load expected tables
# cursor.execute("CREATE TABLE IF NOT EXISTS workflow_info(repo TEXT, run_id INT, run_attempt, status TEXT CHECK(status IN ('successful', 'failed', 'cancelled')) DEFAULT 'failed')")
# cursor.execute("CREATE TABLE IF NOT EXISTS test_results(name TEXT, execution_time REAL, Cpp_standard TEXT, passed_cases INT, failed_cases INT, skipped_cases INT, passed_assertions INT, failed_assertions INT)")



# # terminate connection to database
# connector.commit()
# connector.close()
