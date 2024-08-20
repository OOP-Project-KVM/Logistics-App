import unittest
from unittest.mock import Mock
from commands.assign_package import AssignPackageToRouteCommand
from core.application_data import ApplicationData
from models.package import Package
from models.route import Route
from models.status.route_status import RouteStatus
from datetime import datetime

class TestAssignPackageToRouteCommand(unittest.TestCase):
    
    def setUp(self) :
        self.app_data = Mock(ApplicationData)
        self.package_id = 1001
        self.route_id = 101
        self.command = AssignPackageToRouteCommand([str(self.package_id), str(self.route_id)], self.app_data)

    def test_execute_package_not_found(self):
        self.app_data.get_package_by_id.return_value = None
        self.assertEqual(self.command.execute(), f"Package with ID {self.package_id} not found.")
    
    def test_execute_route_not_found(self):
        self.app_data.get_package_by_id.return_value = Mock(Package)
        self.app_data.get_route_by_id.return_value = None
        self.assertEqual(self.command.execute(), f"Route with ID {self.route_id} not found.")
    
    def test_execute_eta_not_calculated(self):
        package = Mock(Package)
        self.app_data.get_package_by_id.return_value = package
        route = Mock(Route)
        self.app_data.get_route_by_id.return_value = route
        self.app_data.calculate_eta_for_route.return_value = None
        self.assertEqual(self.command.execute(), f"Error: Could not calculate ETA for {package.end_location} on route {route.id}.")

    def test_execute_route_not_pending(self):
        package = Mock(Package)
        route = Mock(Route)
        self.app_data.get_package_by_id.return_value = package
        self.app_data.get_route_by_id.return_value = route
        self.app_data.calculate_eta_for_route.return_value = datetime.now()
        route.status = RouteStatus.INPROGRESS
        self.assertEqual(self.command.execute(), f"Error: You can't assign a package to a route that is In Progress or Completed  .")

    def test_execute_success(self):
        package = Mock(Package)
        route = Mock(Route)
        eta = datetime.now()
        self.app_data.get_package_by_id.return_value = package
        self.app_data.get_route_by_id.return_value = route
        self.app_data.calculate_eta_for_route.return_value = eta
        route.status = RouteStatus.PENDING
        expected_time = eta.strftime('%Y-%m-%d %H:%M')

        route.assign_package = Mock()

        result = self.command.execute()

        route.assign_package.assert_called_once_with(package)
        self.assertEqual(package.expected_arrival_time, expected_time)
        self.assertEqual(result, f"Package {self.package_id} assigned to route {self.route_id} with expected arrival time {expected_time}.")