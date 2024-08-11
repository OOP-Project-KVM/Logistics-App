# Description: Create a new delivery package with unique ID, start location, end location, weight,
# and customer contact information.

# Input: Start location, end location, weight (kg), customer contact information.

# Output: Confirmation of package creation with unique ID.

#VIKTOR

from commands.base_command import BaseCommand
from models.package import Package
from models.location import Location

class CreatePackageCommand(BaseCommand):
    pass