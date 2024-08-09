# Description: View information about all delivery routes, including stops, delivery weight, 
# and current stop based on the time of day.

# Input: None

# Output: List of all routes with details.

from commands.base_command import BaseCommand


class ViewRouteCommand(BaseCommand):
    def execute(self):
        result = self.app_data.view_routes()

        return "There are currently no roads. You have to create roads first." if len(result) == 0 else result