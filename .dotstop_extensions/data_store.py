import sqlite3
from datetime import datetime

def data_store_pull() -> list[dict]:
    data = get_my_data()
    return data

def data_store_push(data: list[dict]):
    push_my_data(data)

def get_my_data() -> list[dict]:
    return []

def push_my_data(data: list[dict]):
    connector = sqlite3.connect("TSF/TemporaryTrustableScoring.db")
    connector.execute("PRAGMA foreign_keys = ON")
    cursor = connector.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS commit_info(date INTEGER PRIMARY KEY, root TEXT, SHA TEXT, tag TEXT, job_id TEXT, schema_version INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS scores(ID TEXT, score REAL, date INTEGER, PRIMARY KEY (ID, date), FOREIGN KEY(date) REFERENCES commit_info(date))")
    # extract data from data
    info = data[0].get("info")
    scores = data[0].get("scores")
    # Currently, the commit date is stored as string.
    # Since the local timezone is used and for comparison, 
    # it would be better to have it as a unix-timestamp.
    datum_string = info.get("Commit date/time")
    datum = int(datetime.strptime(datum_string, "%a %b %d %H:%M:%S %Y").timestamp())
    # check if current commit coincides with existing commit
    cursor.execute("SELECT MAX(date) AS recent_commit FROM commit_info")
    if datum == cursor.fetchone()[0]:
        print("Only the most recent data for each commit are stored. Overwriting obsolete data ...")
    # write commit_info
    root = info.get("Repository root")
    sha = info.get("Commit SHA")
    tag = info.get("Commit tag")
    job_id = info.get("CI job id")
    schema_version = info.get("Schema version")
    command = f"INSERT OR REPLACE INTO commit_info VALUES('{datum}', '{root}', '{sha}', '{tag}', '{job_id}', '{schema_version}')"
    cursor.execute(command)
    connector.commit()
    # write scores
    for score in scores:
        id = score.get("id")
        numerical_score = score.get("score")
        command = f"INSERT OR REPLACE INTO scores VALUES('{id}', {numerical_score}, '{datum}')"
        cursor.execute(command)
    # don't forget to commit!
    connector.commit()
    # terminate data-base connection
    connector.close()
    