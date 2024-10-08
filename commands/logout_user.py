from commands.base_command import BaseCommand
from core.application_data import ApplicationData


class LogoutUserCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        self.app_data.logout()

        return "You logged out!"

