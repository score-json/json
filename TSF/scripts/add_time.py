import sys
import sqlite3
from datetime import datetime
from urllib import request, error
import json

# This is a script, which adds the missing column time to the TestResultData.db
# The reason for this change is a changed rationale with the temporary proof-of-concept implementation of the test-data storage


def from_rest_api(repo, run_id):
    """Query the Actions run object and return run_started_at."""
    url = f"https://api.github.com/repos/{repo}/actions/runs/{run_id}"
    req = request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "gha-run-start-python-script/1.0")
    req.add_header("Authorization", "Bearer {ADD_YOUR_OWN_TOKEN_HERE}")

    try:
        with request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data.get("run_started_at")
    except error.HTTPError as e:
        msg = e.read().decode("utf-8", errors="ignore")
        print(f"HTTP {e.code} when calling GitHub API: {msg}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error calling GitHub API: {e}", file=sys.stderr)
        return None

def column_exists(conn, table, column):
    cur = conn.execute(f"PRAGMA table_info({table})")
    return any(row[1] == column for row in cur.fetchall())  # row[1] = name

# initiate connection to database
connector = sqlite3.connect("TSF/TestResultData.db")
connector.execute("PRAGMA foreign_keys = ON")

if not column_exists(connector, "workflow_info", "time"):
    connector.execute("ALTER TABLE workflow_info ADD COLUMN time INT DEFAULT -1")

cursor = connector.cursor()


cursor.execute("SELECT * FROM workflow_info")
rows = cursor.fetchall()
for row in rows:
    # t = int(datetime.fromisoformat(from_rest_api(row[0],row[1])).timestamp())
    # command = f"UPDATE workflow_info SET time = {t} WHERE repo = \"{row[0]}\" AND run_id = {str(row[1])} AND run_attempt = {str(row[2])}"
    # cursor.execute(command)
    # connector.commit()
    print(row)

connector.commit()
connector.close()