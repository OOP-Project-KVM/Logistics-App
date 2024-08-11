# Description: Assign a free truck to an existing delivery route.

# Input: Truck ID, Route ID.

# Output: Confirmation of truck assignment to the route.

# KALIN

from commands.base_command import BaseCommand

from models.status import Status

class AssignTruckToRouteCommand(BaseCommand):
    def execute(self):
        truck_id = int(self.params[0])
        route_id = int(self.params[1])

        truck = self.app_data.get_truck_by_id(truck_id)  
        if truck is None:
            return f"Error: Truck with ID {truck_id} not found."

        route = self.app_data.get_route_by_id(route_id)  
        if route is None:
            return f"Error: Route with ID {route_id} not found."

        route.assign_truck(truck)
        truck.set_truck_status(Status.BUSY)
        return f"Truck {truck.id} assigned to route {route.id}."
