class Car:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def add_car(self):
        """Add a new car to the database."""
        make = input("Enter car make/brand: ")
        model = input("Enter car model: ")
        year = int(input("Enter car year: "))
        mileage = int(input("Enter car mileage: "))
        available = input("Is car available? (yes/no): ").lower() == 'yes'
        min_rent_period = int(input("Enter minimum rent period (days): "))
        max_rent_period = int(input("Enter maximum rent period (days): "))
        price_per_day = float(input("Enter price per day: "))

        self.cursor.execute('''
            INSERT INTO cars (make, model, year, mileage, available, min_rent_period, max_rent_period, price_per_day)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (make, model, year, mileage, available, min_rent_period, max_rent_period, price_per_day))
        self.conn.commit()
        print("Car added successfully.")

    def update_car_status(self):
        """Update the availability status of a car."""
        car_id = int(input("Enter car ID to update: "))
        available = input("Is car available? (yes/no): ").lower() == 'yes'
        self.cursor.execute("UPDATE cars SET available=? WHERE id=?", (available, car_id))
        self.conn.commit()
        print("Car status updated successfully.")

    def delete_car(self):
        """Delete a car from the database."""
        car_id = int(input("Enter car ID to delete: "))
        confirm = input(f"Are you sure you want to delete car {car_id}? (yes/no): ").lower()
        if confirm == 'yes':
            self.cursor.execute("DELETE FROM cars WHERE id=?", (car_id,))
            self.conn.commit()
            print("Car deleted successfully.")
        else:
            print("Deletion cancelled.")

    def view_all_cars(self):
        """Display all cars in the database."""
        self.cursor.execute("SELECT * FROM cars")
        cars = self.cursor.fetchall()
        print("\n--- All Cars ---")
        for car in cars:
            print(f"ID: {car[0]}, Make: {car[1]}, Model: {car[2]}, Year: {car[3]}, "
                  f"Mileage: {car[4]}, Available: {'Yes' if car[5] else 'No'}, "
                  f"Min Rent: {car[6]} days, Max Rent: {car[7]} days, Price/day: ${car[8]}")

    def edit_user_details(self):
        """Edit user details."""
        username = input("Enter username to edit: ")
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = self.cursor.fetchone()
        if not user:
            print("User not found.")
            return

        print("Leave blank to keep current value.")
        new_last_name = input(f"Enter new last name (current: {user[4]}): ") or user[4]
        new_first_name = input(f"Enter new first name (current: {user[5]}): ") or user[5]
        new_password = input("Enter new password (leave blank to keep current): ") or user[2]
        new_address = input(f"Enter new address (current: {user[6]}): ") or user[6]
        new_phone_number = input(f"Enter new phone number (current: {user[7]}): ") or user[7]

        self.cursor.execute('''
            UPDATE users
            SET last_name=?, first_name=?, password=?, address=?, phone_number=?
            WHERE username=?
        ''', (new_last_name, new_first_name, new_password, new_address, new_phone_number, username))
        self.conn.commit()
        print("User details updated successfully.")