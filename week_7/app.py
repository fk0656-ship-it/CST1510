from auth import register_user, login_user

def display_menu():
    """Display the main menu options."""
    print("\n--- SECURE AUTH SYSTEM ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
