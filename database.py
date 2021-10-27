import sqlite3

def connect_db():
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    db = conn.cursor()
    return db