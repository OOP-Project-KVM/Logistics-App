# Description: View details of a specific package.
# Input: Package ID.
# Output: Details of the package including its current status and route information.
from commands.base_command import BaseCommand
from core.application_data import ApplicationData

class ViewPackageDetails(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        package_id = int(self.params[0])
        result = self.app_data.get_package_by_id(package_id)
        if result:
            return f"Package found:\n{result}"

        else:
            return f"package with ID {package_id} not found!"

