import sqlite3
import os

print("Hallo, Welt!")

if os.path.exists("./artifacts"):
    print("Das war ein voller Erfolg.")
else:
    print("Das war ein voller Griff ins Klo.")