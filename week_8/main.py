from services.user_service import create_users_table, register_user, login_user

# Run database setup
def run_tests():
    # Create the users table
    create_users_table()

    # Optional: Register a new user
    success, msg = register_user("alice", "SecurePass123!")
    print(msg)

    # Login the user
    success, msg = login_user("alice", "SecurePass123!")
    print(msg)

if __name__ == "__main__":
    run_tests()
