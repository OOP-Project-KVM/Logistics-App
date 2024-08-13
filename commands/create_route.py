# Description: Create a new delivery route with a unique ID and a list of locations,
#  including departure and expected arrival times.

# Input: List of locations with departure and expected arrival times.

# Output: Confirmation of route creation with unique ID.

# KALIN

from commands.base_command import BaseCommand
from models.route import Route
from models.location import Location
from core.application_data import ApplicationData
from models.roles import Roles

class CreateRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data):
        super().__init__(params, app_data)


    def execute(self):
        if self.app_data.has_logged_in_user.role == "Manager": # type: ignore
            route_id = int(self.params[0])
            location_names = self.params[1:]

            route = self.app_data.get_route_by_id(route_id)
            if route is not None:
                return f"Error: Route with ID {route_id} already exists."

            locations = [Location(name) for name in location_names]
            self.app_data.create_route(route_id,locations)
            return f"Route {route_id} created."
        else:
            return "you are not a manager"