from models.roles import Roles


class User:
    def __init__(self, username, first_name, last_name, password, user_role, contact):
        self.last_name = self.validate_last_name(last_name)
        self.first_name = self.validate_first_name(first_name)
        self.username = self.validate_username(username)
        self.password = self.validate_password(password)
        self.role = self.role_validator(user_role)
        self.contact = contact

    def role_validator(self, role):
        if role not in [Roles.MANAGER, Roles.WORKER]:
            raise ValueError("non existent role")
        return role

    def validate_first_name(self, first_name):
        if len(first_name) < 2 or len(first_name) > 15:
            raise ValueError("First name has to be [2:15] characters long")
        return first_name

    def validate_last_name(self, last_name):
        if len(last_name) < 2 or len(last_name) > 15:
            raise ValueError("Last name has to be [2:15] characters long")
        return last_name

    def validate_username(self, username):
        if len(username) < 3 or len(username) > 15:
            raise ValueError('Username has to be [3:15] characters long')
        return username

    def validate_password(self, password):
        if len(password) < 8 or len(password) > 15:
            raise ValueError('Password has to be [8:15] characters long')
        return password
