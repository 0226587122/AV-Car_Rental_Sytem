def decoration():
    """Returns a decoration string of asterisks."""
    return '*' * 10

def get_user_role(db, username):
    """Fetches the role of the user based on the username."""
    result = db.fetchone("SELECT role FROM users WHERE username=?", (username,))
    return result[0] if result else None

def choose_role():
    """Prompts the user to choose a role."""
    while True:
        role = input("Choose role (admin/user): ").lower()
        if role in ['admin', 'user']:
            return role
        print("Invalid role. Please choose 'admin' or 'user'.")
