# Description: Create a new delivery route with a unique ID and a list of locations,
#  including departure and expected arrival times.

# Input: List of locations with departure and expected arrival times.

# Output: Confirmation of route creation with unique ID.

# KALIN

from commands.base_command import BaseCommand
from models.route import Route
from models.location import Location


class CreateRouteCommand(BaseCommand):
    def execute(self):
        route_id = int(self.params[0])
        locations = self.params[1:]

        route = self.app_data.get_route_by_id(route_id)
        if route is not None:
            return f"Error: Route with ID {route_id} already exists."

        locations = [Location(location) for location in locations]
        route = Route(route_id, locations)
        self.app_data.create_route(route,locations)
        return f"Route {route_id} created."