from database import get_connection

def get_vehicles():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, license_plate, model, driver, status FROM vehicles")
    results = c.fetchall()
    conn.close()
    return results

def add_vehicle(license_plate, model, driver, status):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO vehicles (license_plate, model, driver, status) VALUES (?, ?, ?, ?)",
              (license_plate, model, driver, status))
    conn.commit()
    conn.close()

def search_vehicles(text):
    conn = get_connection()
    c = conn.cursor()
    pattern = f"%{text}%"
    c.execute("""SELECT id, license_plate, model, driver, status FROM vehicles
                 WHERE license_plate LIKE ? OR model LIKE ? OR driver LIKE ? OR status LIKE ?""",
              (pattern, pattern, pattern, pattern))
    results = c.fetchall()
    conn.close()
    return results