from admin_management import Admin
from user_management import User
from db import initialize_db
from utils import choose_role, decoration

def main():
    initialize_db()

    while True:
        print(decoration(), "--- Car Rental System ---", decoration())
        print("1. Choose Role")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            role = choose_role()
            if role == 'admin':
                Admin.admin_login()
            else:
                user = User()
                username = user.login()
                if username:
                    user.view_available_cars()
        elif choice == '2':
            print(decoration(), "Thank you for using the AV Car Rental!", decoration())
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
