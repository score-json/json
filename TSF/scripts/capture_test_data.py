import sys
import sqlite3

connector = sqlite3.connect("TestResultData.db")
connector.execute("PRAGMA foreign_keys = ON")
cursor = connector.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS workflow_info()")
cursor.execute("CREATE TABLE IF NOT EXISTS test_results(name TEXT)")



connector.commit()
connector.close()
