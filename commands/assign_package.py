# Description: Assign a delivery package to an existing delivery route.

# Input: Package ID, Route ID, Expected arrival time.

# Output: Confirmation of package assignment to the route.

# VIKTOR
from commands.base_command import BaseCommand
from core.application_data import ApplicationData


class AssignPackageToRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        package_id = int(self.params[0])
        route_id = int(self.params[1])

        route = self.app_data.get_route_by_id(route_id)

        if route is None:
            return f"Error: Route with ID {route_id} not found."

        package = self.app_data.get_package_by_id(package_id)  # type: ignore
        if package is None:
            return f"Error: Package with ID {package_id} not found."

        route.assign_package(package)
        return f"Package {package.id} assigned to route {route.id}."
