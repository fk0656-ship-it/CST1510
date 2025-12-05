# main.py
from services.user_service import create_users_table, register_user, login_user

def main():
    # Step 1: Ensure the users table exists
    create_users_table()
    print("Users table is ready.\n")

    while True:
        print("\n=== User System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()
            try:
                success, msg = register_user(username, password)
                print(msg)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            try:
                success, msg = login_user(username, password)
                print(msg)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
