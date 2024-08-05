from models.delivery_system import DeliverySystem
from models.route import Route
from models.truck import Truck
from models.package import Package
from models.location import Location
from core.application_data import ApplicationData

# CreatePackageCommand , ViewUnassignedPackagesCommand, CreateRouteCommand
# SearchRouteCommand , AssignPackageToRouteCommand , ViewRoutesCommand 
# AssignTruckToRouteCommand , ViewAvailableTrucksCommand , 
# ViewPackageDetailsCommand , ViewRouteDetailsCommand


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        command, *params = input_line.split()
        if command == "createpackage":
            return (params, self._app_data)
        elif command == 'createroute':
            return (params, self._app_data)
        elif command == "assigntruck":
            return (params, self._app_data)
        elif command == "assignpackage":
            return (params, self._app_data)
        elif command == "viewroutes":
            return (params, self._app_data)
        elif command == "viewpackages":
            return (params, self._app_data)
        elif command == "viewtrucks":
            return (params, self._app_data)
       