from commands.base_command import BaseCommand


class RegisterUserCommand(BaseCommand):
    def __init__(self, params: list[str], app_data):
        super().__init__(params, app_data)

    def execute(self):
        username = self.params[0]
        first_name = self.params[1]
        last_name = self.params[2]
        password = self.params[3]
        user_role = self.params[4]
        contact = self.params[5]

        user = self.app_data.registrate_user(username, first_name, last_name, password, user_role, contact)
        self.app_data.login(user)
        return f"User with username: {username} registered successfully."