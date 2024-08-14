# Description: View information about all delivery routes, including stops, delivery weight, 
# and current stop based on the time of day.

# Input: None

# Output: List of all routes with details.

from commands.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
     
    def execute(self):
        result = self.app_data.view_routes()
    
        if len(result) == 0:
            return "There are currently no roads. You have to create roads first."
        else:
            return result
        