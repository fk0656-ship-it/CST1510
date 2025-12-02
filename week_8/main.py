from services.user_service import register_user, login_user, migrate_users_from_file
import sqlite3
import pandas as pd
import bcrypt
from pathlib import Path

# Paths
DATA_DIR = Path("DATA")
DB_PATH = DATA_DIR / "intelligence_platform.db"
DATA_DIR.mkdir(parents=True, exist_ok=True)

print("✅ Imports successful!")
print(f"DATA folder: {DATA_DIR.resolve()}")
print(f"Database will be created at: {DB_PATH.resolve()}")


# Database connection
def connect_database(db_path=DB_PATH):
    return sqlite3.connect(str(db_path))

# Create tables
def create_users_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS users
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       username
                       TEXT
                       NOT
                       NULL
                       UNIQUE,
                       password_hash
                       TEXT
                       NOT
                       NULL,
                       role
                       TEXT
                       DEFAULT
                       'user',
                       created_at
                       TIMESTAMP
                       DEFAULT
                       CURRENT_TIMESTAMP
                   )
                   """)
    conn.commit()
    print("✅ Users table created successfully!")


def create_cyber_incidents_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS cyber_incidents
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       date
                       TEXT,
                       incident_type
                       TEXT,
                       severity
                       TEXT,
                       status
                       TEXT,
                       description
                       TEXT,
                       reported_by
                       TEXT,
                       created_at
                       TIMESTAMP
                       DEFAULT
                       CURRENT_TIMESTAMP,
                       FOREIGN
                       KEY
                   (
                       reported_by
                   ) REFERENCES users
                   (
                       username
                   )
                       )
                   """)
    conn.commit()
    print("✅ Cyber incidents table created successfully!")


def create_datasets_metadata_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS datasets_metadata
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       dataset_name
                       TEXT
                       NOT
                       NULL,
                       category
                       TEXT,
                       source
                       TEXT,
                       last_updated
                       TEXT,
                       record_count
                       INTEGER,
                       file_size_mb
                       REAL,
                       created_at
                       TIMESTAMP
                       DEFAULT
                       CURRENT_TIMESTAMP
                   )
                   """)
    conn.commit()
    print("✅ Datasets metadata table created successfully!")


# User functions
def register_user(username, password, role="user"):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return False, f"Username '{username}' already exists."
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    password_hash = hashed.decode('utf-8')
    cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                   (username, password_hash, role))
    conn.commit()
    conn.close()
    return True, f"User '{username}' registered successfully!"


def login_user(username, password):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    if not user:
        return False, "Username not found."
    stored_hash = user[2]
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
        return True, f"Welcome, {username}!"
    return False, "Invalid password."


# Cyber incident functions
def insert_incident(conn, date, incident_type, severity, status, description, reported_by=None):
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO cyber_incidents
                       (date, incident_type, severity, status, description, reported_by)
                   VALUES (?, ?, ?, ?, ?, ?)
                   """, (date, incident_type, severity, status, description, reported_by))
    conn.commit()
    return cursor.lastrowid


def get_all_incidents(conn):
    return pd.read_sql_query("SELECT * FROM cyber_incidents", conn)


def update_incident_status(conn, incident_id, new_status):
    cursor = conn.cursor()
    cursor.execute("UPDATE cyber_incidents SET status = ? WHERE id = ?", (new_status, incident_id))
    conn.commit()
    return cursor.rowcount


def delete_incident(conn, incident_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cyber_incidents WHERE id = ?", (incident_id,))
    conn.commit()
    return cursor.rowcount


def get_incidents_by_type_count(conn):
    return pd.read_sql_query("""
                             SELECT incident_type, COUNT(*) as count
                             FROM cyber_incidents
                             GROUP BY incident_type
                             ORDER BY count DESC
                             """, conn)


def get_high_severity_by_status(conn):
    return pd.read_sql_query("""
                             SELECT status, COUNT(*) as count
                             FROM cyber_incidents
                             WHERE severity = 'High'
                             GROUP BY status
                             ORDER BY count DESC
                             """, conn)


def get_incident_types_with_many_cases(conn, min_count=5):
    return pd.read_sql_query("""
                             SELECT incident_type, COUNT(*) as count
                             FROM cyber_incidents
                             GROUP BY incident_type
                             HAVING COUNT (*) > ?
                             ORDER BY count DESC
                             """, conn, params=(min_count,))


# Database setup

def setup_database():
    conn = connect_database()
    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    conn.close()
    print("✅ Database setup complete!")


# Run tests
def run_tests():
    print("\n🧪 Running tests...")
    setup_database()
    success, msg = register_user("test_user", "TestPass123!")
    print(f"Register user: {msg}")
    success, msg = login_user("test_user", "TestPass123!")
    print(f"Login user: {msg}")

    conn = connect_database()
    incident_id = insert_incident(conn, "2025-12-01", "Test Incident", "High", "Open",
                                  "This is a test", "test_user")
    print(f"Inserted incident ID: {incident_id}")
    df = get_all_incidents(conn)
    print(df)
    update_incident_status(conn, incident_id, "Resolved")
    delete_incident(conn, incident_id)
    conn.close()
    print("✅ All tests completed!")


# Main
if __name__ == "__main__":
    run_tests()
