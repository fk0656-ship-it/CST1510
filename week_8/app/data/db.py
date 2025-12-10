import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "users.db"

def connect_database():
    """Connect to SQLite database (creates file if it doesn't exist)."""
    conn = sqlite3.connect(DB_FILE)
    return conn
