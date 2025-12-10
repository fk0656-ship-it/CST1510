import bcrypt
from pathlib import Path
import sqlite3

DB_PATH = "data/users.db"

def connect_database():
    return sqlite3.connect(DB_PATH)

def create_users_table():
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    """)
    conn.commit()
    conn.close()

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
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
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
    with open(filepath, 'r') as f:
        lines = f.readlines()
    conn = connect_database()
    cursor = conn.cursor()
    migrated_count = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) != 2:
            continue
        username, password_hash = parts
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                (username, password_hash, 'user')
            )
            if cursor.rowcount > 0:
                migrated_count += 1
        except Exception:
            continue
    conn.commit()
    conn.close()
    return True, f"Migrated {migrated_count} users from {filepath}"
