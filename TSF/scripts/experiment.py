import sqlite3
import os

print("Hallo, Welt!")

sha = os.getenv("GITHUB_SHA")
ubuntu_artifact = f"./artifacts/ubuntu-{str(sha)}"
print(ubuntu_artifact)
if not os.path.exists(ubuntu_artifact):
    print("Satz mit x.")
else:
    os.system(f"cd artifacts/ubuntu-{str(sha)}")
    os.system("ls")
    os.system("cd ..")
    os.system("echo 'nice try, meiner'")
    ubuntu_artifact += "/TestResults.db"
    table = "test_results"
    connector = sqlite3.connect(ubuntu_artifact)
    cursor = connector.cursor()
    # check whether our results can be accessed
    cursor.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,))
    if cursor.fetchone() is None:
        # if not, it is not trustable
        print("Is Scheiße, wa?")
    if True:
        # our result table can be read
        tests = ["moin", "test_class_lexer"]
        score = 0.0
        expected_tests = len(tests)
        warnings = []
        for test in tests:
            command = f"SELECT COUNT(*) FROM {table} WHERE name = ?"
            if cursor.execute(command, (test)) is None:
                warnings.append(Warning(f"Could not find data for test {test}."))
                continue
            command = f"""
                        SELECT
                            COALESCE(SUM(passed_cases), 0) AS total_passed,
                            COALESCE(SUM(failed_cases), 0) AS total_failed
                        FROM {table}
                        WHERE name = ?
                    """
            passed, failed = cursor.execute(command, (test,)).fetchone()
            score += float(passed)/((float(passed)+float(failed))*expected_tests)
        print("Toll!")
        print(score)