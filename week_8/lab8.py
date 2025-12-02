# lab8.py (NO pandas version)
import sqlite3
from datetime import datetime
import hashlib

DB_FILE = "lab8.db"

# --- Database Setup ---
def connect_database():
    return sqlite3.connect(DB_FILE)

def create_all_tables(conn):
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    # Incidents table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            incident_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT NOT NULL,
            description TEXT,
            reported_by TEXT
        )
    """)

    conn.commit()
    print("✅ Tables created")

# --- User Functions ---
def insert_user(username, password_hash, role='user'):
    conn = connect_database()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                       (username, password_hash, role))
        conn.commit()
        print(f"User '{username}' added.")
    except sqlite3.IntegrityError:
        print(f"❌ User '{username}' already exists!")
    finally:
        conn.close()

def get_user_by_username(username):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

# --- Incident Functions ---
def insert_incident(date, incident_type, severity, status, description, reported_by=None):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO incidents (date, incident_type, severity, status, description, reported_by)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (date, incident_type, severity, status, description, reported_by))

    conn.commit()
    incident_id = cursor.lastrowid
    conn.close()
    print(f"Incident ID {incident_id} added.")
    return incident_id

def get_all_incidents():
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents")
    rows = cursor.fetchall()
    conn.close()
    return rows

# --- Main ---
def main():
    conn = connect_database()
    create_all_tables(conn)
    conn.close()

    password_hash = hashlib.sha256("mypassword123".encode()).hexdigest()
    insert_user("alice", password_hash, "admin")

    print("User:", get_user_by_username("alice"))

    insert_incident(str(datetime.today().date()), "Phishing", "High", "Open", "Testing incident", "alice")

    incidents = get_all_incidents()
    print("\nAll incidents:")
    for row in incidents:
        print(row)

if __name__ == "__main__":
    main()

