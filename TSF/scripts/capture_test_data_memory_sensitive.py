import sys
import sqlite3
import os
import xml.etree.ElementTree as ET
import re
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

def clean_test_case(testcase: str) -> tuple[str,str]:
    # This function expects a testcase of the form "testcase_name_cppxx".
    # It returns the tuple ["testcase_name","gnu++xx"].
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
    raw_data = input[0]
    data = re.findall(r'(\d+)\s+(passed|failed|skipped)\b', raw_data)
    if len(data) < 5:
        raise RuntimeError("Fatal Error: Received incomplete or wrong result table.")
    metadata["passed test cases"] = int(data[0][0])
    metadata["failed test cases"] = int(data[1][0])
    metadata["skipped test cases"] = int(data[2][0])
    metadata["passed assertions"] = int(data[3][0])
    metadata["failed assertions"] = int(data[4][0])
    return metadata


def get_metadata(testcase: ET.Element) -> dict:
    # expects testcase extracted from a junit xml-file as input
    # extracts the data interesting to us
    # Assumption of Use: before execution, it is checked if is_unit_test(testcase)==True
    metadata = dict()
    # from name both name of the test and C++ standard can be extracted
    unsplit_name = testcase.get("name", None)
    if unsplit_name is None:
        raise RuntimeError("Fatal error: Can not read name of test-case!")
    name, standard = clean_test_case(unsplit_name)
    metadata["name"] = name
    metadata["standard"] = standard
    metadata["execution time"] = float(testcase.get("time"))
    # results are not as easily extracted but must be processed further
    metadata = metadata | read_result_table(list(testcase.find("system-out").itertext()))
    return metadata

def is_unit_test(testcase: ET.Element) -> bool:
    # crude test if the element belongs to a unit-test
    return "_cpp" in testcase.get('name')

def get_all_xml_files(directory: str = '.') -> list[str]:
    # search the folder containing all the artifacts and list the paths of expected test-reports
    result = []
    try:
        content = os.listdir(directory)
    except FileNotFoundError as e:
        print(e)
        return result
    for entry in content:
        if os.path.isdir(directory+'/'+entry):
            result = result + get_all_xml_files(directory+'/'+entry)
        if entry.endswith('.xml'):
            file = directory+'/'+entry if directory != '.' else entry
            result.append(file)
    return result

def get_ctest_target(log_name: str) -> str:
    # extracts name of ctest target from junit log
    # log_name has the form "path/to/log/file/target_junit.xml", and target is expected
    log = log_name.split('/')[-1]
    return log.removesuffix("_junit.xml")

def find_most_recent_results(target: str, name: str, compiler: str, cpp_standard: str, database: sqlite3.Connection) -> list[int]:
    cursor = database.cursor()
    cursor.execute("""
                    WITH combination AS (
                        SELECT workflow_info.repo, workflow_info.run_id, workflow_info.run_attempt, workflow_info.time
                        FROM test_results INNER JOIN workflow_info ON
                        workflow_info.repo = test_results.repo 
                        AND workflow_info.run_id = test_results.run_id 
                        AND workflow_info.run_attempt = test_results.run_attempt
                        WHERE test_results.ctest_target = ? AND test_results.name = ? AND test_results.compiler = ? AND test_results.cpp_standard = ?
                    )
                    SELECT repo, run_id, run_attempt FROM combination
                    ORDER BY time DESC, run_id DESC, run_attempt DESC
                    LIMIT 1;
                    """,(target,name,compiler,cpp_standard))
    result = cursor.fetchone()
    if result is None:
        # if no recent run is found, data need to be stored
        return [] 
    repo, run_id, run_attempt = result
    cursor.execute("""
                    SELECT passed_cases, failed_cases, skipped_cases, passed_assertions, failed_assertions 
                    FROM test_results WHERE
                    ctest_target = ? AND name = ? AND compiler = ? AND cpp_standard = ? AND repo = ? AND run_id = ? AND run_attempt = ?
                    """, (target,name,compiler,cpp_standard,repo,run_id,run_attempt))
    result = cursor.fetchone()
    return [] if result is None else list(result)

##########################
# Below starts the script.
##########################

if __name__ == "__main__":

    # check if argument was delivered
    if len(sys.argv) != 2:
        raise RuntimeError("Expected status of workflow as argument. Aborting!")
    # expected argument: status of workflow
    # check if the argument has the expected form
    status = sys.argv[1]
    if status not in ["successful", "failed", "cancelled"]:
        raise RuntimeError("The input does not match the expected format! Permissible are 'successful', 'failed' and 'cancelled'. Aborting!")

    # get environment variables
    try:
        environment = setup_environment_variables()
    except RuntimeError as e:
        raise RuntimeError("Critical error: Can not uniquely identify environment data! Aborting recording of data.")
    
    # Step 1: store metadata of workflow run persistently

    # initiate connection to database
    connector = sqlite3.connect("TSF/MemoryEfficientTestResultData.db")
    connector.execute("PRAGMA foreign_keys = ON")

    # load expected tables
    # table workflow_info contains metadata of workflow and is updated every time
    command = (
        "CREATE TABLE IF NOT EXISTS workflow_info(",
        "repo TEXT, ",                              # repository
        "run_id INT, ",                             # ID of workflow run
        "run_attempt INT, ",                        # Attempt-number of workflow run
        "status TEXT ",                             # Termination-status of workflow                                         
        "CHECK(status IN ('successful', 'failed', 'cancelled')) DEFAULT 'failed', ",
        "time INT, ",                               # the time that is associated to this workflow run
        "PRIMARY KEY(repo, run_id, run_attempt))"
    )
    connector.execute(''.join(command))
    # table test_results contains detailed results for each individual test
    command = (
        "CREATE TABLE IF NOT EXISTS test_results(",
        "ctest_target TEXT, ",                      # name of the ctest target located in ci.cmake
        "name TEXT, ",                              # name of the test
        "execution_time REAL, ",                    # execution time in seconds
        "compiler TEXT, ",                          # compiler information
        "cpp_standard TEXT, ",                      # cpp-standard
        "passed_cases INT, ",                       # number of passed test-cases
        "failed_cases INT, ",                       # number of failed test-cases
        "skipped_cases INT, ",                      # number of skipped test-cases
        "passed_assertions INT, ",                  # number of passed assertions
        "failed_assertions INT, ",                  # number of failed assertions
        "repo TEXT, ",                              # repository
        "run_id INT, ",                             # ID of workflow run
        "run_attempt INT, ",                        # Attempt-number of workflow run
        "FOREIGN KEY(repo, run_id, run_attempt) REFERENCES workflow_info);"
        )
    connector.execute(''.join(command))
    cursor = connector.cursor()

    # Count number of rows as heuristic size-checker.
    # In case that the update-check fails, and every result is stored, allow for approximately 26 complete results to be stored
    cursor.execute("SELECT MAX(COALESCE((SELECT MAX(rowid) FROM workflow_info),0),COALESCE((SELECT MAX(rowid) FROM test_results),0));")
    if cursor.fetchone()[0] > 1e5:
        connector.close()
        raise RuntimeError("The persistent data storage is too large! Please move persistent data to external storage.")

    # fill in metadata
    # OBSERVE: This script expects the status of the github workflow as argument
    repo = environment.get('GITHUB_REPOSITORY')
    run_id = environment.get('GITHUB_RUN_ID')
    run_attempt = environment.get('GITHUB_RUN_ATTEMPT')
    time = int(datetime.now(timezone.utc).timestamp())
    command = "INSERT INTO workflow_info VALUES(?,?,?,?,?)"
    cursor.execute(command,(repo, run_id, run_attempt, status, time))
    # Don't forget to save!
    connector.commit()
    
    # Step 2: generate report of most recent test run and update persistent storage if necessary
    
    # initialise database connection
    conn = sqlite3.connect("MemoryEfficientTestResults.db")
    cur = conn.cursor()
    # add the expected table
    # the table TestResults.test_results differs from TestResultData.test_results in that the metadata of the commit are not saved.
    command = (
        "CREATE TABLE IF NOT EXISTS test_results(",
        "ctest_target TEXT, ",                      # name of the ctest target located in ci.cmake
        "name TEXT, ",                              # name of the test
        "execution_time REAL, ",                    # execution time in seconds
        "compiler TEXT, ",                          # compiler information
        "cpp_standard TEXT, ",                      # cpp-standard
        "passed_cases INT, ",                       # number of passed test-cases
        "failed_cases INT, ",                       # number of failed test-cases
        "skipped_cases INT, ",                      # number of skipped test-cases
        "passed_assertions INT, ",                  # number of passed assertions
        "failed_assertions INT",                    # number of failed assertions
        ")"
        )
    conn.execute(''.join(command))

    # Load my artifacts
    junit_logs = get_all_xml_files("./my_artifacts/")

    #extract data
    for junit_log in junit_logs:
        tree = ET.parse(junit_log)
        file_root = tree.getroot()
        testsuite = next(file_root.iter('testsuite'), None)
        if testsuite is None:
            print(f"Error: Could not find testsuite data in {junit_log}.")
            continue
        for testcase in (case for case in file_root.iter('testcase') if is_unit_test(case)):
            metadata = get_metadata(testcase)
            target = get_ctest_target(junit_log)
            compiler = testsuite.get('name')
            more_compiler_info = [case for case in file_root.iter('testcase') if case.get("name") == "cmake_target_include_directories_configure"]
            if len(more_compiler_info) != 0:
                compiler_information = more_compiler_info[0]
                information = list(compiler_information.find("system-out").itertext())[0].split('\n')[0]
                compiler = information.replace("-- The CXX compiler identification is ","")
            name = metadata.get('name')
            cpp_standard = metadata.get('standard')
            data = (
                        target,
                        name,
                        metadata.get('execution time'), 
                        compiler, 
                        cpp_standard, 
                        metadata.get('passed test cases'), 
                        metadata.get('failed test cases'), 
                        metadata.get('skipped test cases'), 
                        metadata.get('passed assertions'), 
                        metadata.get('failed assertions')
                    )
            command ="INSERT INTO test_results VALUES(?,?,?,?,?,?,?,?,?,?);"
            cur.execute(command, data)
            conn.commit()
            most_recently_stored_results = find_most_recent_results(target,name,compiler,cpp_standard,connector)
            current_results = [metadata.get('passed test cases'),metadata.get('failed test cases'),metadata.get('skipped test cases'),metadata.get('passed assertions'),metadata.get('failed assertions')]
            if (len(most_recently_stored_results) != 5) or any(most_recently_stored_results[i]!=current_results[i] for i in range(0,5)):
                data = data + (repo, run_id, run_attempt)
                command ="INSERT INTO test_results VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);"
                cursor.execute(command,data)

                
    # terminate connection to temporary database
    # don't forget to commit the changes
    conn.commit()
    conn.close()

    # terminate connection to persistent database
    # don't forget to commit the changes again, for good measure
    connector.commit()
    connector.close()
