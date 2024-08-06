


class User:
    def __init__(self, username, password, role):
        self.username = self.validate_username(username)
        self.password = self.validate_password(password)
        self.role = role

    def validate_username(self, username):
        if len(username) < 3 or len(username) > 15:
            return False
        return username

    def validate_password(self, password):
        if len(password) < 8 or len(password) > 15:
            return False
        return password
    