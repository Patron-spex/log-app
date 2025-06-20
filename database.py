import sqlite3

DB_NAME = "logistik.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY,
        license_plate TEXT,
        model TEXT,
        driver TEXT,
        status TEXT
    )''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS chat (
        id INTEGER PRIMARY KEY,
        sender TEXT,
        message TEXT,
        time TEXT
    )''')
    conn.commit()
    conn.close()