from models.roles import Roles
from commands.validation_helpers import (validate_last_name, validate_first_name, validate_username,
                                          validate_password, role_validator, validate_contact)

class User:
    def __init__(self, username, first_name, last_name, password, user_role, contact):
        self.last_name = validate_last_name(last_name)
        self.first_name = validate_first_name(first_name)
        self.username = validate_username(username)
        self.password = validate_password(password)
        self.role = role_validator(user_role)
        self.contact = validate_contact(contact)