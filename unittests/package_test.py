import unittest
from datetime import datetime
from models.package import Package
from models.status.package_status import PackageStatus



class TestPackage(unittest.TestCase):

    def setUp(self):
        Package.all_ids.clear()
        """if we don't use this it won't work because it is using the same id. Don't know how to fix it """
        Package.customer_info.clear()


        self.valid_id = "PKG001"
        self.valid_start = "MEL"
        self.valid_end = "SYD"
        self.valid_weight = 10.5
        self.valid_contact = "1234567890"
        self.package = Package(
            self.valid_id,
            self.valid_start,
            self.valid_end,
            self.valid_weight,
            self.valid_contact
        )

    def test_create_package_success(self):
        # Test successful package creation
        self.assertEqual(self.package.id, self.valid_id)
        self.assertEqual(self.package.start_location, self.valid_start)
        self.assertEqual(self.package.end_location, self.valid_end)
        self.assertEqual(self.package.weight, self.valid_weight)
        self.assertEqual(self.package.customer_contact, self.valid_contact)
        self.assertEqual(self.package.distance, 877)  # Expected distance from SYD to MEL
        self.assertEqual(self.package.pack_status, PackageStatus.TOBEASSIGNED)
        self.assertIsNone(self.package.expected_arrival_time)

    def test_invalid_id(self):
        # Test invalid package ID
        with self.assertRaises(ValueError) as context:
            Package(None, self.valid_start, self.valid_end, self.valid_weight, self.valid_contact)
        self.assertEqual(str(context.exception), "You must provide ID")

        Package.all_ids.add(self.valid_id)
        with self.assertRaises(ValueError) as context:
            Package(self.valid_id, self.valid_start, self.valid_end, self.valid_weight, self.valid_contact)
        self.assertEqual(str(context.exception), f"Shipment ID {self.valid_id} already exists.")

    def test_invalid_location(self):
        # Test invalid start and end location
        Package.all_ids.clear()
        invalid_location = "XYZ"
        with self.assertRaises(ValueError) as context:
            Package(self.valid_id, invalid_location, self.valid_end, self.valid_weight, self.valid_contact)
        self.assertEqual(str(context.exception), "We don't provide services at this location.")

        with self.assertRaises(ValueError) as context:
            Package(self.valid_id, self.valid_start, invalid_location, self.valid_weight, self.valid_contact)
        self.assertEqual(str(context.exception), "We don't provide services at this location.")

    def test_invalid_weight(self):
        Package.all_ids.clear()
        # Test invalid weight
        with self.assertRaises(ValueError) as context:
            Package(self.valid_id, self.valid_start, self.valid_end, -5, self.valid_contact)
        self.assertEqual(str(context.exception), "Weight must be a positive number.")

        with self.assertRaises(ValueError) as context:
            Package(self.valid_id, self.valid_start, self.valid_end, -1, self.valid_contact)
        self.assertEqual(str(context.exception), "Weight must be a positive number.")

    def test_invalid_customer_contact(self):
        Package.all_ids.clear()
        # Test invalid customer contact
        with self.assertRaises(ValueError) as context:
            Package(self.valid_id, self.valid_start, self.valid_end, self.valid_weight, "123")
        self.assertEqual(str(context.exception), "Customer contact info  must be between 5 and 20 characters!")

        with self.assertRaises(ValueError) as context:
            Package(self.valid_id, self.valid_start, self.valid_end, self.valid_weight, "123456789012345678901")
        self.assertEqual(str(context.exception), "Customer contact info  must be between 5 and 20 characters!")

    def test_invalid_location_change(self):
        # Test changing location to an invalid one
        invalid_location = "XYZ"
        with self.assertRaises(ValueError) as context:
            self.package.start_location = invalid_location
        self.assertEqual(str(context.exception), "We don't provide services at this location.")

    def test_set_expected_arrival_time(self):
        # Test setting the expected arrival time
        future_time = datetime(2024, 12, 31, 15, 0, 0)
        self.package.set_expected_arrival_time(future_time)
        self.assertEqual(self.package.expected_arrival_time, future_time)

    def test_package_str(self):
        # Test the string representation of the package
        expected_str = (f"Package Details:\n"
                        f"ID: {self.package.id}\n"
                        f"From: {self.package.start_location}\n"
                        f"To: {self.package.end_location}\n"
                        f"Distance: {self.package.distance}km\n"
                        f"Weight: {self.package.weight} kg\n"
                        f"Status: {self.package.pack_status.value}\n"
                        f"Customer Contact: {self.package.customer_contact}")
        self.assertEqual(str(self.package), expected_str)

    def test_same_start_end_location(self):
        Package.all_ids.clear()
        # Test the case where start and end locations are the same
        with self.assertRaises(ValueError) as context:
            Package(self.valid_id, self.valid_start, self.valid_start, self.valid_weight, self.valid_contact)
        self.assertEqual(str(context.exception), "The start and end address must be in different locations.")


if __name__ == '__main__':
    unittest.main()
