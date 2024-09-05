from db import Database
from utils import decoration

class User:
    def __init__(self, username="", password="", last_name="", first_name="", address="", phone_number=""):
        self.username = username
        self.password = password
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number

    def register_user(self, db):
        """Registers a new user in the database."""
        db.execute('''INSERT INTO users (username, password, role, last_name, first_name, address, phone_number)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (self.username, self.password, 'user', self.last_name, self.first_name, self.address, self.phone_number))
        print("User registered successfully.")

    @staticmethod
    def login(db):
        """Logs in the user by checking credentials."""
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_login = db.fetchone("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        if user_login:
            print(f"Welcome, {username}!")
            return username
        else:
            print("Invalid credentials, please check your username and password.")
            return None

    @staticmethod
    def view_available_cars(db):
        """Displays available cars."""
        cars = db.fetchall("SELECT * FROM cars WHERE available=1")
        print(decoration(), "---Available Cars---", decoration())
        for car in cars:
            print(f"ID: {car[0]}, Make: {car[1]}, Model: {car[2]}, Year: {car[3]}, "
                  f"Mileage: {car[4]}, Min Rent: {car[6]} days, Max Rent: {car[7]} days, "
                  f"Price/day: ${car[8]}")

    @staticmethod
    def view_rent_history(db, user_id):
        """Displays the rent history of the user."""
        bookings = db.fetchall(
            "SELECT * FROM bookings b JOIN users u ON b.user_id = u.id JOIN cars ON b.car_id = cars.id WHERE b.user_id=?",
            (user_id,))
        print(decoration(), "---Rent History---", decoration())
        for booking in bookings:
            print(f"ID: {booking[0]}, User_ID: {booking[1]}, Username: {booking[8]}, Car_ID: {booking[2]}, "
                  f"Start Date: {booking[3]}, End Date: {booking[4]}, Total Rent Price: {booking[5]}, Rental Status: {booking[6]}")
