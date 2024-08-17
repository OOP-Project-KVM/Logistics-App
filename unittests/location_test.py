import unittest

from models.location import Location


class TestLocation(unittest.TestCase):

    def setUp(self):
        self.valid_location_name = "SYD"
        self.invalid_location_name = "XYZ"

    def test_valid_location_name(self):
        location = Location(self.valid_location_name)
        self.assertEqual(location.name, self.valid_location_name)

    def test_invalid_location_name(self):
        with self.assertRaises(ValueError) as context:
            Location(self.invalid_location_name)
        self.assertEqual(str(context.exception), "We don't provide services there.")

    def test_str_representation(self):
        location = Location(self.valid_location_name)
        expected_str = "---Location Details---\nName: SYD\n"
        self.assertEqual(str(location), expected_str)
