import unittest
from models.truck import Truck
from models.status.truck_status import Status


class TestTruck(unittest.TestCase):

    def setUp(self):
        """
        Initialize the Truck object before each test.
        """
        self.truck = Truck(id=1001, model='Scania', capacity=42000, max_range=8000)

    def test_initialization(self):
        """
        Test the initialization of the Truck object.
        """
        self.assertEqual(self.truck.id, 1001)
        self.assertEqual(self.truck.model, 'Scania')
        self.assertEqual(self.truck.capacity, 42000)
        self.assertEqual(self.truck.max_range, 8000)
        self.assertEqual(self.truck.is_free, Status.AVAILABLE)

    def test_set_availability(self):
        """
        Test setting the availability status of the Truck object.
        """
        self.truck.is_free = Status.AVAILABLE
        self.assertEqual(self.truck.is_free, Status.AVAILABLE)

        self.truck.is_free = Status.BUSY
        self.assertEqual(self.truck.is_free, Status.BUSY)

    def test_string_representation(self):
        """
        Test the string representation of the Truck object.
        """
        expected_string = (
            f"Truck 1001: Scania,\n"
            f"42000 kg, 8000 km\n"
        )
        self.assertEqual(str(self.truck), expected_string)


if __name__ == '__main__':
    unittest.main()
