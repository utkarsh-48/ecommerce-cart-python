import json
import os

def load_users():
    if os.path.exists("users.json"):
        with open("users.json","r") as f:
            return json.load(f)
    return {}
def save_user(users):
    with open("users.json","w") as f:
        json.dump(users,f)

def register():
    users = load_users()
    while True:
        username = input("Enter the Username: ").strip()
        if username in users:
            print("Username already exists, Try a different One.")
            continue
        if not username:
            print("Username can`t be Empty")
            continue
        else:
           while True:
            password = input("Enter Password: ").strip()
            if not password:
                 print("Password can`t be empty")
            else:
                users[username] = {"password":password}
                save_user(users)
                print(f"Welcome to the Community, {username} ")
                return username

def login():
    users = load_users()
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    if username in users and users[username]["password"] == password:
        print(f"Welcome Back {username}")
        return username
    else:
        print("Invalid Credentials")
        return None
