import sqlite3

# initialise connection to persistent storage
connector = sqlite3.connect("TrustableScoring.db")
connector.execute("PRAGMA foreign_keys = ON")
target_cursor = connector.cursor()
target_cursor.execute("CREATE TABLE IF NOT EXISTS commit_info(date INTEGER PRIMARY KEY, root TEXT, SHA TEXT, tag TEXT, job_id TEXT, schema_version INTEGER)")
target_cursor.execute("CREATE TABLE IF NOT EXISTS scores(ID TEXT, score REAL, date INTEGER, PRIMARY KEY (ID, date), FOREIGN KEY(date) REFERENCES commit_info(date))")

# initialise connection to temporary storage
importer = sqlite3.connect("TemporaryTrustableScoring.db")
importer.execute("PRAGMA foreign_keys = ON")
source_cursor = importer.cursor()

# read  temporary storage
source_cursor.execute("SELECT * FROM commit_info")
commit_info_rows = source_cursor.fetchall()
source_cursor.execute("SELECT * FROM scores")
score_rows = source_cursor.fetchall()

# write permanent storage
if commit_info_rows:
    target_cursor.executemany("INSERT OR REPLACE INTO commit_info (date, root, SHA, tag, job_ID, schema_version) VALUES (?, ?, ?, ?, ?, ?)", commit_info_rows)
    # don't forget to save
    connector.commit
if score_rows:
    target_cursor.executemany("INSERT OR REPLACE INTO scores (ID, score, date) VALUES (?, ?, ?)", score_rows)
    # don't forget to save!
    connector.commit
# terminate connections
connector.close()
importer.close()