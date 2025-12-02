from services.user_service import create_users_table, register_user, login_user, migrate_users_from_file
from pathlib import Path
import sqlite3

# Ensure data folder exists
DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "intelligence_platform.db"

# Database connection
def connect_database():
    return sqlite3.connect(str(DB_PATH))

# Setup database
def setup_database():
    conn = connect_database()
    create_users_table(conn)
    conn.close()
    print("✅ Database setup complete!")

# Run tests
def run_tests():
    setup_database()

    # Optional: migrate users from file
    success, msg = migrate_users_from_file()  # only if you have data/users.txt
    print(msg)

    # Register a new user
    success, msg = register_user("alice", "SecurePass123!", "analyst")
    print(msg)

    # Login the user
    success, msg = login_user("alice", "SecurePass123!")
    print(msg)

if __name__ == "__main__":
    run_tests()
