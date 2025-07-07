def init_db():
    import sqlite3

    # Verbindung zur Datenbank herstellen (oder erstellen, falls sie nicht existiert)
    conn = sqlite3.connect('logistik_dashboard.db')
    cursor = conn.cursor()

    # Tabellen erstellen, falls sie nicht existieren
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        status TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        upload_date TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS analytics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        metric TEXT NOT NULL,
        value REAL NOT NULL
    )
    ''')

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()