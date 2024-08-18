from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.user import User


class LoginUserCommand(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        
        if len(self.params) != 2:
            raise ValueError("Error: Invalid number of parameters. Expected 2 parameters.")
        username, password = self.params
        
        
        user = self._app_data.find_user_by_username(username)
        if user.password != password:  #type: ignore
            return f"Wrong username or password!"
        else:
            self._app_data.login(user)

            return f'User {user.username} successfully logged in!'   #type: ignore
