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
    # initialise data-base connection
    connector = sqlite3.connect("TSF/TrustableScoring.db")
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
        # remove duplicate
        cursor.execute("DELETE FROM scores WHERE date=recent_commit")
        cursor.execute("DELETE FROM commit_info WHERE date=recent_commit")
    # write commit_info
    root = info.get("Repository root")
    sha = info.get("Commit SHA")
    tag = info.get("Commit tag")
    job_id = info.get("CI job id")
    schema_version = info.get("Schema version")
    command = f"INSERT INTO commit_info VALUES('{datum}', '{root}', '{sha}', '{tag}', '{job_id}', '{schema_version}')"
    cursor.execute(command)
    connector.commit()
    # write scores
    for score in scores:
        id = score.get("id")
        numerical_score = score.get("score")
        command = f"INSERT INTO scores VALUES('{id}', {numerical_score}, '{datum}')"
        cursor.execute(command)
    connector.commit()
    # terminate data-base connection
    connector.close()