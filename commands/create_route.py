# Description: Create a new delivery route with a unique ID and a list of locations,
#  including departure and expected arrival times.

# Input: List of locations with departure and expected arrival times.

# Output: Confirmation of route creation with unique ID.

# KALIN

from commands.base_command import BaseCommand
from models.location import Location
from datetime import datetime
from models.status.roles import Roles

class CreateRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data):
        super().__init__(params, app_data)

    def execute(self):
        if self.app_data.has_logged_in_user.role == Roles.MANAGER.value :  # type: ignore
            route_id = int(self.params[0])
            location_names = [loc.upper() for loc in self.params[1:]]

            route = self.app_data.get_route_by_id(route_id)
            if route is not None:
                return f"Error: Route with ID {route_id} already exists."

            # Prompt for departure date and time
            departure_date_input = input("Enter the departure date (YYYY-MM-DD): ")
            departure_time_input = input("Enter the departure time (HH:MM): ")

            # Combine the date and time inputs into a datetime object
            departure_time = datetime.strptime(f"{departure_date_input} {departure_time_input}", "%Y-%m-%d %H:%M")

            locations = [Location(name) for name in location_names]

            # Create the route with the specified departure time
            self.app_data.create_route(route_id, locations, departure_time)

            return f"Route {route_id} created with departure time {departure_time.strftime('%Y-%m-%d %H:%M')}."
        else:
            return "You are not authorized to create routes."