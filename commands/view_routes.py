# Description: View information about all delivery routes, including stops, delivery weight, 
# and current stop based on the time of day.

# Input: None

# Output: List of all routes with details.

from datetime import datetime
from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.roles import Roles



class ViewRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
     
    def execute(self):
        if self.app_data.has_logged_in_user.role == Roles.MANAGER.value:  # type: ignore
            routes = self.app_data.routes
            # self.app_data.check_in_progress_routes()
            output = ""
            for route in routes:
                route.check_and_unload_packages()
                self.app_data.calculate_eta_for_route(route)
                
                output += f"Route ID: {route.id}\n"
                
                
                output += f"Route Info: {route.route_info()}\n"
                

                    


       
            return output
        else:
            return "You are not authorized to view routes."
