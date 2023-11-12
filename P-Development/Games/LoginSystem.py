# created using GPT

import bcrypt

class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

def register(username, password):
    # Hash the password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Create a new user instance
    new_user = User(username, password_hash)

    # Save the user data to a database or file
    save_user(new_user)

def save_user(user):
    # In a real system, you would save the user data to a database or file
    # For simplicity, let's just print the user information here
    print(f"User '{user.username}' registered successfully.")

def login(username, password):
    # Retrieve user data from the database or file
    user = get_user(username)

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash):
        print(f"Login successful. Welcome, {user.username}!")
    else:
        print("Invalid username or password.")

def get_user(username):
    # In a real system, you would retrieve user data from a database or file
    # For simplicity, let's hardcode a user here
    return User(username, b'$2b$12$MSm8OSFLVpJNIDR6sHzI6.UVjw.5yjyLoAa8pt91uyYDEA7x9Qq4C')

# Example usage
register("user1", "password123")  # Register a user
login("user1", "password123")     # Login with correct credentials

def bank():
    print("")
    balance = int(input("Deposit amount: "))
    while balance > 10000:
        print("Too much or not valid amount!")
        print("")
        balance = int(input("Deposit amount: "))
        print(balance)
    if balance > 10000:
        str(balance)
        print("")
        print("Too much or not valid amount!")
    else:
        str(balance)
        print("")
        print("Deposited, $" + balance + "!")
        quit()

        
bank()
