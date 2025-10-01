import sqlite3

if __name__ == "__main__":

    connector = sqlite3.connect("TSF/MemoryEfficientTestResultData.db")
    connector.execute("PRAGMA foreign_keys = ON")
    cursor = connector.cursor()
    cursor.executescript("""
        CREATE TABLE test_results_copy(
        ctest_target TEXT,
        name TEXT,
        execution_time REAL,
        compiler TEXT,
        cpp_standard TEXT,
        passed_cases INT,
        failed_cases INT,
        skipped_cases INT,
        passed_assertions INT,
        failed_assertions INT,
        repo TEXT,
        run_id INT,
        run_attempt INT,
        FOREIGN KEY(repo, run_id, run_attempt) REFERENCES workflow_info);
    """)
    cursor.executescript("""
    INSERT INTO test_results_copy SELECT * FROM test_results;
    DROP TABLE test_results;
    ALTER TABLE test_results_copy RENAME TO test_results;
    """)
    connector.commit()
    connector.close()