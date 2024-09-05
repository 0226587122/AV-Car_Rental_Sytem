from car_management import Car
from rental_management import ManageBookings
from utils import decoration

class Admin:
    @staticmethod
    def admin_login():
        """Handles admin login."""
        username_admin = "admin"
        password_admin = "admin123"

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == username_admin and password == password_admin:
            print("Login successful!")
            Admin.admin_page()
        else:
            print("Invalid credentials, please check your username and password.")

    @staticmethod
    def admin_page():
        """Displays the admin page with various options."""
        while True:
            print(decoration(), "--- Admin Menu ---", decoration())
            print("1. Add Car")
            print("2. Update Car Status")
            print("3. Delete Car")
            print("4. View Pending Bookings")
            print("5. View Approved Bookings")
            print("6. Manage Bookings")
            print("7. View All Cars")
            print("8. Edit User Details")
            print("9. Logout")
            admin_choice = input("Enter your choice: ")

            if admin_choice == '1':
                car = Car()
                car.make = input("Enter car make/brand: ")
                car.model = input("Enter car model: ")
                car.year = int(input("Enter car year: "))
                car.mileage = int(input("Enter car mileage: "))
                car.available = int(input("Is car available? (1 for Yes, 0 for No): "))
                car.min_rent_period = int(input("Enter minimum rent period (days): "))
                car.max_rent_period = int(input("Enter maximum rent period (days): "))
                car.price_per_day = float(input("Enter price per day: "))
                car.add_car()

            elif admin_choice == '2':
                car = Car()
                print(decoration(), "---Update Car Status---", decoration())
                car.car_id = int(input("Enter car ID to update: "))
                car.available = int(input("Updated car status? (1 for Available, 0 for Rented/Unavailable): "))
                car.update_car_status()

            elif admin_choice == '3':
                car = Car()
                print(decoration(), "---Deleting a Car---", decoration())
                car.car_id = int(input("Enter car ID to delete: "))
                confirmation = input(f"Are you sure you want to delete Car ID {car.car_id}? (YES/NO): ").upper()
                if confirmation == "YES":
                    car.delete_car()
                else:
                    continue

            elif admin_choice == '4':
                ManageBookings.view_pending_bookings()

            elif admin_choice == '5':
                ManageBookings.view_approved_bookings()

            elif admin_choice == '6':
                ManageBookings.manage_bookings()

            elif admin_choice == '7':
                Car.view_all_cars()

            elif admin_choice == '8':
                Car.edit_user_details()

            elif admin_choice == '9':
                print(decoration(), "Thank you for using the AV Car Rental!", decoration())
                exit()
