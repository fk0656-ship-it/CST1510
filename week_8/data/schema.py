from .db import connect_database

def create_tables():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        );
    """)

    conn.commit()
    conn.close()
    print("✓ Users table created successfully.")

if __name__ == "__main__":
    create_tables()
