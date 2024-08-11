# Description: Assign a delivery package to an existing delivery route.

# Input: Package ID, Route ID, Expected arrival time.

# Output: Confirmation of package assignment to the route.

# VIKTOR

from commands.base_command import BaseCommand
from models.status import Status
from models.package import Package

class AssignPackageToRouteCommand(BaseCommand):
    pass