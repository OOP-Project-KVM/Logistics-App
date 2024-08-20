import unittest
from datetime import datetime, timedelta
from models.route import Route
from models.package import Package
from models.truck import Truck
from models.status.package_status import PackageStatus
from models.status.truck_status import Status
from models.status.route_status import RouteStatus
from models.location import Location


class TestRoute(unittest.TestCase):

    def setUp(self):
        Package.all_ids.clear()

        self.trucks = [
                          Truck(id, 'Scania', 42000, 8000) for id in range(1001, 1011)
                      ] + [
                          Truck(id, 'MAN', 37000, 10000) for id in range(1011, 1026)
                      ] + [
                          Truck(id, 'Actros', 26000, 13000) for id in range(1026, 1041)
                      ]


        self.location1 = Location("SYD")
        self.location2 = Location("MEL")
        self.location3 = Location("ADL")


        self.truck = self.trucks[0]


        self.package1 = Package("PKG001", "SYD", "MEL", 100, "1234567890")
        self.package2 = Package("PKG002", "MEL", "ADL", 300, "0987654321")
        self.package3 = Package("PKG003", "MEL", "ADL", 100000, "0987654323")

        self.route = Route(1, [self.location1, self.location2, self.location3])
        

    def test_initial_route_properties(self):
        self.assertEqual(self.route.id, 1)
        self.assertEqual(self.route.locations, [self.location1, self.location2, self.location3])
        self.assertIsNone(self.route.truck)
        self.assertEqual(self.route.packages, [])
        self.assertIsNone(self.route.current_eta)
        self.assertEqual(self.route.current_load, 0.0)
        self.assertEqual(self.route.status, RouteStatus.PENDING)

    def test_assign_truck_success(self):
        self.route.assign_truck(self.truck)
        self.assertEqual(self.route.truck, self.truck)
        self.assertEqual(self.route.current_load, 0.0)

    def test_assign_truck_fail_not_available(self):
        self.truck.is_free = Status.BUSY
        with self.assertRaises(ValueError) as context:
            self.route.assign_truck(self.truck)
        self.assertEqual(str(context.exception), "Truck is not available.")

    def test_has_capacity(self):
        self.route.assign_truck(self.truck)
        self.assertTrue(self.route.has_capacity(self.package1.weight))
        self.assertFalse(self.route.has_capacity(self.package1.weight + 1232312312))

    def test_assign_package_success(self):
        self.route.assign_truck(self.truck)
        self.route.assign_package(self.package1)
        self.assertIn(self.package1, self.route.packages)
        self.assertEqual(self.route.current_load, self.package1.weight)
        self.assertEqual(self.package1.pack_status, PackageStatus.OUTFORDELIVERY)

    def test_assign_package_fail_no_truck(self):
        with self.assertRaises(ValueError) as context:
            self.route.assign_package(self.package1)
        self.assertEqual(str(context.exception), "Cannot assign package to a route with no truck assigned.")

    def test_assign_package_fail_capacity_exceeded(self):
        self.route.assign_truck(self.truck)
        self.route.assign_package(self.package1)
        with self.assertRaises(ValueError) as context:
            self.route.assign_package(self.package3)
        self.assertEqual(str(context.exception), "Route cannot accept this package: capacity exceeded.")

    def test_assign_package_fail_already_assigned(self):
        self.route.assign_truck(self.truck)
        self.route.assign_package(self.package1)
        with self.assertRaises(ValueError) as context:
            self.route.assign_package(self.package1)
        self.assertEqual(str(context.exception), "Package is already assigned to this route.")

    
    def test_set_arrival_time(self):
        arrival_time = datetime.now() + timedelta(days=2)
        self.route.arrival_time = arrival_time
        self.assertEqual(self.route.arrival_time, arrival_time)

    def test_set_departure_time(self):
        departure_time = datetime.now() + timedelta(hours=1)
        self.route.departure_time = departure_time
        self.assertEqual(self.route.departure_time, departure_time)

    def test_change_route_status(self):
        self.route.status = RouteStatus.PENDING
        self.assertEqual(self.route.status, RouteStatus.PENDING)
        self.route.status = RouteStatus.COMPLETED
        self.assertEqual(self.route.status, RouteStatus.COMPLETED)

    def test_change_locations(self):
        new_location = Location("BRI")
        self.route.locations = [self.location1, self.location2, new_location]
        self.assertEqual(self.route.locations, [self.location1, self.location2, new_location])

    def test_max_capacity(self):
        self.route.assign_truck(self.truck)
        self.assertEqual(self.route.max_capacity, self.truck.capacity)


if __name__ == '__main__':
    unittest.main()
