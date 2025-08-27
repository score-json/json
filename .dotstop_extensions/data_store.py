import sqlite3
from datetime import datetime
import os

# global variable -- path to persistent data storage
persistent_storage = "TSF/TrustableScoring.db"

def data_store_pull() -> list[dict]:
    data = get_my_data()
    return data

def data_store_push(data: list[dict]):
    push_my_data(data)

def get_my_data() -> list[dict]:
    # check if persistent data has been loaded
    if not os.path.exists(persistent_storage):
        return []
    # initialise connection to persistent storage
    connector = sqlite3.connect(persistent_storage)
    connector.execute("PRAGMA foreign_keys = ON")
    cursor = connector.cursor()
    # initialise tables, if not exist
    cursor.execute("CREATE TABLE IF NOT EXISTS commit_info(date INTEGER PRIMARY KEY, root TEXT, SHA TEXT, tag TEXT, job_id TEXT, schema_version INTEGER, branch_name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS scores(ID TEXT, score REAL, date INTEGER, PRIMARY KEY (ID, date), FOREIGN KEY(date) REFERENCES commit_info(date))")
    # initialise my_data
    my_data = []
    # read commit_info
    cursor.execute("SELECT * FROM commit_info") 
    commit_info = cursor.fetchall()
    for info in commit_info:
        command = f"SELECT * FROM scores WHERE date=={info[0]}"
        cursor.execute(command)
        scores = cursor.fetchall()
        date = datetime.fromtimestamp(info[0])
        date_as_string = date.strftime("%a %b %d %H:%M:%S %Y")
        if len(info) == 6:
            branch_name = ""
        else:
            branch_name = info[6] if info[6]!=None else ""
        commit = {"Repository root": info[1],
                  "Commit SHA": info[2],
                  "Commit date/time": date_as_string, 
                  "Commit tag": info[3],
                  "CI job id": info[4],
                  "Schema version": info[5],
                  "Branch name": branch_name
                }
        score_data = []
        for score in scores:
            score_datum = {"id": score[0], "score": score[1]}
            score_data.append(score_datum)
        my_datum = {"scores": score_data, "info": commit}
        my_data.append(my_datum)
    return my_data

def push_my_data(data: list[dict]):
    # It is assumed that the folder containing the persistent storage does exist.
    # initialise connection to persistent storage; if database itself does not exist, then create
    connector = sqlite3.connect(persistent_storage)
    connector.execute("PRAGMA foreign_keys = ON")
    cursor = connector.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS commit_info(date INTEGER PRIMARY KEY, root TEXT, SHA TEXT, tag TEXT, job_id TEXT, schema_version INTEGER, branch_name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS scores(ID TEXT, score REAL, date INTEGER, PRIMARY KEY (ID, date), FOREIGN KEY(date) REFERENCES commit_info(date))")
    cursor.execute("PRAGMA table_info(commit_info);")
    columns = [pragma_info[1] for pragma_info in cursor.fetchall()]
    # branch_name was first forgotten
    if "branch_name" not in columns:
        cursor.execute("ALTER TABLE commit_info ADD COLUMN branch_name TEXT DEFAULT ''")
        connector.commit()
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
    branch_name = info.get("Branch name")
    command = f"INSERT OR REPLACE INTO commit_info VALUES('{datum}', '{root}', '{sha}', '{tag}', '{job_id}', '{schema_version}', '{branch_name}')"
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
    