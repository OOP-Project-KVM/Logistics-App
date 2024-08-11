# Description: Create a new delivery package with unique ID, start location, end location, weight,
# and customer contact information.

# Input: Start location, end location, weight (kg), customer contact information.

# Output: Confirmation of package creation with unique ID.

#VIKTOR
from commands.base_command import BaseCommand
from models.package import Package


class CreatePackageCommand(BaseCommand):
    def execute(self):
        if len(self.params) != 5:
            return "Error: Invalid number of parameters. Expected 5 parameters."

        id_pack = self.params[0]
        start_location = self.params[1].upper()
        end_location = self.params[2].upper()
        weight = float(self.params[3])
        customer_contact = self.params[4]

        new_package = Package(id_pack, start_location, end_location, weight, customer_contact)
        self.app_data.create_package(new_package)

        return f"Package {id_pack} created successfully."