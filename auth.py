import json
import os

USERS_FILE = "users.json"

def load_users():
    """Load users from the JSON file."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_user(users):
    """Save users to the JSON file."""
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def register():
    """Register a new user."""
    users = load_users()
    while True:
        username = input("Enter the Username: ").strip()
        if username in users:
            print("Username already exists, Try a different One.")
            continue
        if not username:
            print("Username can't be empty")
            continue
        while True:
            password = input("Enter Password: ").strip()
            if not password:
                print("Password can't be empty")
            else:
                # WARNING: Passwords are stored in plain text!
                users[username] = {"password": password}
                save_user(users)
                print(f"Welcome to the Community, {username}")
                return username

def login():
    """Login an existing user."""
    users = load_users()
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    if username in users and users[username]["password"] == password:
        print(f"Welcome Back {username}")
        return username
    else:
        print("Invalid Credentials")
        return None