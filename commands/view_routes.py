# Description: View information about all delivery routes, including stops, delivery weight, 
# and current stop based on the time of day.

# Input: None

# Output: List of all routes with details.

from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.roles import Roles


class ViewRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
     
    def execute(self):
        if self.app_data.has_logged_in_user.role == Roles.MANAGER.value:  # type: ignore
            self.app_data.check_in_progress_routes()  # Update route statuses
            routes = self.app_data.get_routes_inProgress()

            for route in routes:
                self.app_data.check_and_unload_packages(route)  # Unload packages and update statuses

            result = self.app_data.view_routes()

            if len(result) == 0:
                return "There are currently no roads. You have to create roads first."
            else:
                return result
        else:
            return "You are not authorized to view routes."
