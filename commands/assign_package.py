# Description: Assign a delivery package to an existing delivery route.

# Input: Package ID, Route ID, Expected arrival time.

# Output: Confirmation of package assignment to the route.

# VIKTOR

from re import S
from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.status.route_status import RouteStatus


class AssignPackageToRouteCommand(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        

    def execute(self):
        package_id = str(self.params[0])
        route_id = int(self.params[1])  
    

        try:
            # Get the package and route from ApplicationData
            package = self.app_data.get_package_by_id(package_id)
            route = self.app_data.get_route_by_id(route_id)
            
            if package is None:
                return f"Package with ID {package_id} not found."
            
            if route is None:
                return f"Route with ID {route_id} not found."
            
            eta_for_city = self.app_data.calculate_eta_for_route(route)

            if eta_for_city is None:
                return f"Error: Could not calculate ETA for {package.end_location} on route {route.id}."
            
            if route.status != RouteStatus.PENDING:
                return f"Error: You can't assign a package to a route that is In Progress or Completed  ."
            
            package.expected_arrival_time = eta_for_city.strftime('%Y-%m-%d %H:%M') 
            route.assign_package(package)
            
            
            return f"Package {package_id} assigned to route {route_id} with expected arrival time {package.expected_arrival_time}."
        
        except ValueError as e:
            return str(e)