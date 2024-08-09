# Description: Search for a suitable delivery route based on the package's start and end locations.

# Input: Package start location, package end location.

# Output: List of matching routes with details

from commands.base_command import BaseCommand

class SearchRouteCommand(BaseCommand):
    def execute(self):

        start_location = self.params[0].strip().upper()
        end_location = self.params[1].strip().upper()

        result = self.app_data.search_route(start_location, end_location)

        return result