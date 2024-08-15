
from commands.base_command import BaseCommand
from models.package_status import PackageStatus


class ViewUnassignedPackagesCommand(BaseCommand):
    def __init__(self, params: list[str], app_data):
        super().__init__(params, app_data)

    def execute(self):
        unassigned_packages = [package for package in self.app_data.packages if package.pack_status == PackageStatus.TOBEASSIGNED]
        if not unassigned_packages:
            return "No unassigned packages found."
        else:
            return "\n".join(f'{package.__str__()}' for package in unassigned_packages)
    
           