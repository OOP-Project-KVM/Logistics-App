import unittest
from unittest.mock import Mock
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from commands.assign_package import AssignPackageToRouteCommand
from commands.login_user import LoginUserCommand
from commands.logout_user import LogoutUserCommand
from commands.register_user import RegisterUserCommand
from commands.view_packageDetails import ViewPackageDetails
from commands.search_route import SearchRouteCommand
from commands.create_route import CreateRouteCommand
from commands.view_routes import ViewRouteCommand
from commands.assign_truck_toRoute import AssignTruckToRouteCommand
from commands.create_package import CreatePackageCommand
from commands.view_unassignedPackages import ViewUnassignedPackagesCommand
from commands.view_free_Trucks import ViewFreeTrucksCommand


class CommandFactory_Should(unittest.TestCase):
    def setUp(self):
        self.app_data = Mock(ApplicationData)
        self.factory = CommandFactory(self.app_data)

    def test_create_valid_commands(self):
        valid_commands = {
            "createpackage": CreatePackageCommand,
            'createroute': CreateRouteCommand,
            "assigntrucktoroute": AssignTruckToRouteCommand,
            "assignpackage": AssignPackageToRouteCommand,
            "viewroutes": ViewRouteCommand,
            "viewpackagedetails": ViewPackageDetails,
            'registeruser': RegisterUserCommand,
            'loginuser': LoginUserCommand,
            'logoutuser': LogoutUserCommand,
            "searchroute": SearchRouteCommand,
            'viewunassignedpackages': ViewUnassignedPackagesCommand,
            'viewavailabletrucks': ViewFreeTrucksCommand,
        }

        for command_name, command_class in valid_commands.items():
            with self.subTest(command_name):
                command_instance = self.factory.create(command_name)
                self.assertIsInstance(command_instance, command_class)

    def test_app_data_is_initialized(self):
        command = self.factory.create("viewroutes")
        self.assertEqual(command._app_data, self.app_data) # type: ignore