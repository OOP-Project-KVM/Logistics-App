LOCATIONS = ["SYD", "MEL", "ADL", "ASP", "BRI", "DAR", "PER"]
from models.roles import Roles
    
def role_validator(role):
    if role not in [Roles.MANAGER.value, Roles.WORKER.value]:
        raise ValueError("non existent role")
    return role

def validate_first_name(first_name):
    if len(first_name) < 2 or len(first_name) > 15:
        raise ValueError("First name has to be [2:15] characters long")
    return first_name

def validate_last_name(last_name):
    if len(last_name) < 2 or len(last_name) > 15:
        raise ValueError("Last name has to be [2:15] characters long")
    return last_name

def validate_username(username):
    if len(username) < 3 or len(username) > 15:
        raise ValueError('Username has to be [3:15] characters long')
    return username

def validate_password(password):
    if len(password) < 8 or len(password) > 15:
        raise ValueError('Password has to be [8:15] characters long')
    return password

def validate_contact(contact):
    if "@" in contact:
        return contact
    raise ValueError("Enter your email address!")

def validate_location(location):
    if location[:3].upper() not in LOCATIONS:
        raise ValueError("We don't provide services at this location.")
    return location

def validate_weight(weight):
    if not isinstance(weight, (int, float)) or weight <= 0:
        raise ValueError("Weight must be a positive number.")
    return weight

def validate_customer_contact(customer_contact):
    if not 5 <= len(customer_contact) <= 20:
        raise ValueError("Customer contact info  must be between 5 and 20 characters!")
    return customer_contact

def validate_locations(start_location, end_location):
    if start_location.upper() == end_location.upper():
        raise ValueError("The start and end address must be in different locations.")