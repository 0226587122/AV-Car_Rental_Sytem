import sqlite3

class Database:
    def __init__(self, db_name='avcrsdb.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

    def execute(self, query, params=()):
        with self.conn:
            self.cursor.execute(query, params)
            self.conn.commit()

    def fetchone(self, query, params=()):
        with self.conn:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()

    def fetchall(self, query, params=()):
        with self.conn:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()

# Initialize database and create tables
def initialize_db():
    with Database() as db:
        db.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT,
            last_name TEXT,
            first_name TEXT,
            address TEXT,
            phone_number TEXT)''')

        db.execute('''CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY,
            make TEXT,
            model TEXT,
            year INTEGER,
            mileage INTEGER,
            available INTEGER,
            min_rent_period INTEGER,
            max_rent_period INTEGER,
            price_per_day REAL)''')

        db.execute('''CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            car_id INTEGER,
            start_date TEXT,
            end_date TEXT,
            total_price REAL,
            status TEXT)''')
