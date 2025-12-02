import bcrypt
from pathlib import Path
import sqlite3
import pandas as pd

DB_PATH = "data/users.db"

def connect_database():
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_all_tables(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            type TEXT,
            severity TEXT,
            status TEXT,
            description TEXT,
            reported_by TEXT
        )
    """)
    conn.commit()

def insert_user(username, password_hash, role='user'):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
        (username, password_hash, role)
    )
    conn.commit()
    conn.close()

def get_user_by_username(username):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def register_user(username, password, role='user'):
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    insert_user(username, password_hash, role)
    return True, f"User '{username}' registered successfully."

def login_user(username, password):
    user = get_user_by_username(username)
    if not user:
        return False, "User not found."
    stored_hash = user[2]
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
        return True, "Login successful!"
    return False, "Incorrect password."

def migrate_users_from_file(filepath='data/users.txt'):
    if not Path(filepath).exists():
        return False, f"File not found: {filepath}"
    with open(filepath, 'r') as file:
        users = file.readlines()
    migrated_count = 0
    for line in users:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) != 2:
            continue
        username, password_hash = parts
        insert_user(username, password_hash)
        migrated_count += 1
    return True, f"Migrated {migrated_count} users from {filepath}"

def insert_incident(date, type_, severity, status, description, reported_by):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO incidents (date, type, severity, status, description, reported_by) VALUES (?, ?, ?, ?, ?, ?)",
        (date, type_, severity, status, description, reported_by)
    )
    conn.commit()
    incident_id = cursor.lastrowid
    conn.close()
    return incident_id

def get_all_incidents():
    conn = connect_database()
    df = pd.read_sql_query("SELECT * FROM incidents", conn)
    conn.close()
    return df

def main():
    print("=" * 60)
    print("Week 8: Database Demo")
    print("=" * 60)

    conn = connect_database()
    create_all_tables(conn)
    conn.close()

    success, msg = migrate_users_from_file()
    print(msg)

    success, msg = register_user("alice", "SecurePass123!", "analyst")
    print(msg)
    success, msg = login_user("alice", "SecurePass123!")
    print(msg)

    incident_id = insert_incident(
        "2024-11-05",
        "Phishing",
        "High",
        "Open",
        "Suspicious email detected",
        "alice"
    )
    print(f"Created incident #{incident_id}")

    df = get_all_incidents()
    print(f"Total incidents: {len(df)}")
    print(df)

if __name__ == "__main__":
    main()
