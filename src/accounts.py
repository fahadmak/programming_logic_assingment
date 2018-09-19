accounts = {"maka": "fahad"}  # dictionary where key is the  password and value is User

# Write a function adds user details to accounts


def add_account(name, password):
    """
    Adds the key value pair to the accounts dictionary
    """
    if not name:
        return "Please fill missing fields"
    if name in list(accounts.values()):
        return "This name already exists"
    if not password:
        return "Please fill missing fields"
    if password in accounts:
        return "This password already exists"
    accounts[password] = name
    return "Account successfully registered"


def login(name, password):
    """
    returns true if the password and corresponding name exist in the 
    accounts dictionary
    """
    if not name:
        return "Please fill missing fields"
    if name not in accounts.values():
        return "Password does not exist"
    if not password:
        return "Please fill missing fields"
    if password not in accounts:
        return "Password does not exist"
    return "You are successfully Logged In"

