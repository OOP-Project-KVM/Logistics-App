import unittest
from unittest.mock import Mock
from commands.assign_truck_toRoute import AssignTruckToRouteCommand
from core.application_data import ApplicationData
from models.truck import Truck
from models.route import Route
from models.truck_status import Status

class TestAssignTruckToRouteCommand(unittest.TestCase):

    def setUp(self):
        # Create mock ApplicationData object
        self.app_data = Mock(spec=ApplicationData)
        self.truck_id = 1001
        self.route_id = 2001
        self.command = AssignTruckToRouteCommand([str(self.truck_id), str(self.route_id)], self.app_data)

    def test_execute_success(self):
        # Setup truck and route mocks
        truck = Mock(spec=Truck)
        truck.id = self.truck_id
        truck.is_free = Status.AVAILABLE
        
        route = Mock(spec=Route)
        route.id = self.route_id

        # Set the mock return values
        self.app_data.get_truck_by_id.return_value = truck
        self.app_data.get_route_by_id.return_value = route

        # Execute the command
        result = self.command.execute()

        # Verify
        self.assertEqual(result, f"Truck {truck.id} assigned to route {route.id}.")
        self.assertEqual(truck.is_free, Status.BUSY)
        route.assign_truck.assert_called_once_with(truck)

    def test_execute_truck_not_found(self):
        # Mock the scenario where the truck is not found
        self.app_data.get_truck_by_id.return_value = None

        # Execute the command
        result = self.command.execute()

        # Verify the result
        self.assertEqual(result, f"Error: Truck with ID {self.truck_id} not found.")

    def test_execute_route_not_found(self):
        # Setup truck mock
        truck = Mock(spec=Truck)
        truck.id = self.truck_id
        truck.is_free = Status.AVAILABLE

        # Mock the scenario where the route is not found
        self.app_data.get_truck_by_id.return_value = truck
        self.app_data.get_route_by_id.return_value = None

        # Execute the command
        result = self.command.execute()

        # Verify the result
        self.assertEqual(result, f"Error: Route with ID {self.route_id} not found.")

    def test_execute_truck_busy(self):
        # Setup truck mock as busy
        truck = Mock(spec=Truck)
        truck.id = self.truck_id
        truck.is_free = Status.BUSY

        # Setup route mock
        route = Mock(spec=Route)
        route.id = self.route_id

        # Set the mock return values
        self.app_data.get_truck_by_id.return_value = truck
        self.app_data.get_route_by_id.return_value = route

        # Execute the command
        result = self.command.execute()

        # Verify the result
        self.assertEqual(truck.is_free, Status.BUSY)  # Truck status should not change
        route.assign_truck.assert_not_called()  # Route should not attempt to assign the truck
        self.assertEqual(result, f"Error: Truck {self.truck_id} is not available.")

