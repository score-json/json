import sys
import sqlite3
import os.path

if os.path.isdir("./my_first_artifact"): print("Moin!")

# connector = sqlite3.connect("TestResultData.db")
# connector.execute("PRAGMA foreign_keys = ON")
# cursor = connector.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS workflow_info(  status ENUM('successful', 'failed', 'cancelled'))")
# cursor.execute("CREATE TABLE IF NOT EXISTS test_results(name TEXT)")



# connector.commit()
# connector.close()
