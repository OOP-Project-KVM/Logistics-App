from commands.assign_package import AssignPackageToRouteCommand
from commands.login_user import LoginUserCommand
from commands.logout_user import LogoutUserCommand
from commands.register_user import RegisterUserCommand
from commands.view_packageDetails import ViewPackageDetails
from core.application_data import ApplicationData
from commands.search_route import SearchRouteCommand
from commands.create_route import CreateRouteCommand
from commands.view_routes import ViewRouteCommand
from commands.assign_truck_toRoute import AssignTruckToRouteCommand
from commands.create_package import CreatePackageCommand
from commands.view_unassignedPackages import ViewUnassignedPackagesCommand
from commands.view_free_Trucks import ViewFreeTrucksCommand

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
        elif command.lower() == "viewpackagedetails":
            return ViewPackageDetails(params, self._app_data)
        elif command.lower() == 'registeruser':
            return RegisterUserCommand(params, self._app_data)
        elif command.lower() == 'loginuser':
            return LoginUserCommand(params, self._app_data)
        elif command.lower() == 'logoutuser':
            return LogoutUserCommand(params, self._app_data)
        elif command.lower() == "searchroute":
            return SearchRouteCommand(params, self._app_data)
        elif command.lower() == 'viewunassignedpackages':
            return ViewUnassignedPackagesCommand(params, self._app_data)
        elif command.lower() == 'viewavailabletrucks':
            return ViewFreeTrucksCommand(params, self._app_data)
        elif command.lower() == 'viewpackagedetails':
            return ViewPackageDetails(params, self._app_data)
       