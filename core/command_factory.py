from commands.assign_package import AssignPackageToRouteCommand
from core.application_data import ApplicationData
from commands.search_route import SearchRouteCommand
from commands.create_route import CreateRouteCommand
from commands.view_routes import ViewRouteCommand
from commands.assign_truck_toRoute import AssignTruckToRouteCommand
from commands.create_package import CreatePackageCommand

# CreatePackageCommand , ViewUnassignedPackagesCommand, CreateRouteCommand
# SearchRouteCommand , AssignPackageToRouteCommand , ViewRoutesCommand 
# AssignTruckToRouteCommand , ViewAvailableTrucksCommand , 
# ViewPackageDetailsCommand , ViewRouteDetailsCommand


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        command, *params = input_line.split()
        if command.lower() == "createpackage":
            return CreatePackageCommand(params, self._app_data)
        elif command.lower() == 'createroute':
            return CreateRouteCommand(params, self._app_data)
        elif command.lower() == "assigntrucktoroute":
            return AssignTruckToRouteCommand(params, self._app_data)
        elif command.lower() == "assignpackage":
            return AssignPackageToRouteCommand(params, self._app_data)
        elif command.lower() == "viewroutes":
            return ViewRouteCommand(params, self._app_data)
        # elif command.lower() == "viewpackagedetails":
        #     return (params, self._app_data)
        # elif command.lower() == "viewtrucks":
        #     return (params, self._app_data)
        elif command.lower() == "searchroute":
            return SearchRouteCommand(params, self._app_data)
       