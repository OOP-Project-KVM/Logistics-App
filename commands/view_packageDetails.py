# Description: View details of a specific package.
# Input: Package ID.
# Output: Details of the package including its current status and route information.
from commands.base_command import BaseCommand
from core.application_data import ApplicationData

class ViewPackageDetails(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        package_id = self.params[0]
        package = self.app_data.get_package_by_id(package_id) 
        if package:
            return f"{package.__str__()}"

        else:
            return f"Package with ID {package_id} not found!"

