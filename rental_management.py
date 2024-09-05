from datetime import datetime


class ManageBookings:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def view_pending_bookings(self):
        """Display pending bookings."""
        self.cursor.execute('''
            SELECT b.*, u.username, c.make, c.model
            FROM bookings b
            JOIN users u ON b.user_id = u.id
            JOIN cars c ON b.car_id = c.id
            WHERE b.status='pending'
        ''')
        bookings = self.cursor.fetchall()
        print("\n--- Pending Bookings ---")
        for booking in bookings:
            print(f"Booking ID: {booking[0]}, User: {booking[8]}, Car: {booking[9]} {booking[10]}, "
                  f"Dates: {booking[3]} to {booking[4]}, Total Price: ${booking[5]}")

    def view_approved_bookings(self):
        """Display approved bookings."""
        self.cursor.execute('''
            SELECT b.*, u.username, c.make, c.model
            FROM bookings b
            JOIN users u ON b.user_id = u.id
            JOIN cars c ON b.car_id = c.id
            WHERE b.status='approved'
        ''')
        bookings = self.cursor.fetchall()
        print("\n--- Approved Bookings ---")
        for booking in bookings:
            print(f"Booking ID: {booking[0]}, User: {booking[8]}, Car: {booking[9]} {booking[10]}, "
                  f"Dates: {booking[3]} to {booking[4]}, Total Price: ${booking[5]}")

    def manage_bookings(self):
        """Manage booking requests."""
        self.cursor.execute('''
            SELECT b.*, u.username, c.make, c.model
            FROM bookings b
            JOIN users u ON b.user_id = u.id
            JOIN cars c ON b.car_id = c.id
            WHERE b.status='pending'
        ''')
        bookings = self.cursor.fetchall()

        if not bookings:
            print("No pending bookings.")
            return

        print("\n--- Manage Bookings ---")
        for booking in bookings:
            print(f"Booking ID: {booking[0]}, User: {booking[8]}, Car: {booking[9]} {booking[10]}, "
                  f"Dates: {booking[3]} to {booking[4]}, Total Price: ${booking[5]}")
            action = input("Approve, Reject, or Return? (a/r/ret): ").lower()

            if action == 'a':
                self.update_booking_status(booking[0], 'approved')
                self.update