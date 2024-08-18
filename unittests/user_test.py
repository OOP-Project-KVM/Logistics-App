import unittest
from models.roles import Roles
from models.user import User  # Adjust import based on actual file structure

class TestUser(unittest.TestCase):

    def setUp(self):

        self.valid_username = "johndoe"
        self.valid_first_name = "John"
        self.valid_last_name = "Doe"
        self.valid_password = "secureP@ssw0rd"
        self.valid_role = Roles.MANAGER.value
        self.valid_contact = "johndoe@gmail.com"

    def test_create_valid_user(self):
        user = User(
            self.valid_username,
            self.valid_first_name,
            self.valid_last_name,
            self.valid_password,
            self.valid_role,
            self.valid_contact
        )
        self.assertEqual(user.username, self.valid_username)
        self.assertEqual(user.first_name, self.valid_first_name)
        self.assertEqual(user.last_name, self.valid_last_name)
        self.assertEqual(user.password, self.valid_password)
        self.assertEqual(user.role, self.valid_role)
        self.assertEqual(user.contact, self.valid_contact)

    def test_invalid_first_name(self):
        with self.assertRaises(ValueError):
            User(
                self.valid_username,
                "J",
                self.valid_last_name,
                self.valid_password,
                self.valid_role,
                self.valid_contact
            )

        with self.assertRaises(ValueError):
            User(
                self.valid_username,
                "J" * 16,
                self.valid_last_name,
                self.valid_password,
                self.valid_role,
                self.valid_contact
            )

    def test_invalid_last_name(self):
        with self.assertRaises(ValueError):
            User(
                self.valid_username,
                self.valid_first_name,
                "D",
                self.valid_password,
                self.valid_role,
                self.valid_contact
            )

        with self.assertRaises(ValueError):
            User(
                self.valid_username,
                self.valid_first_name,
                "D" * 16,
                self.valid_password,
                self.valid_role,
                self.valid_contact
            )

    def test_invalid_username(self):
        with self.assertRaises(ValueError):
            User(
                "Jd",
                self.valid_first_name,
                self.valid_last_name,
                self.valid_password,
                self.valid_role,
                self.valid_contact
            )

        with self.assertRaises(ValueError):
            User(
                "JD" * 8,
                self.valid_first_name,
                self.valid_last_name,
                self.valid_password,
                self.valid_role,
                self.valid_contact
            )

    def test_invalid_password(self):
        with self.assertRaises(ValueError):
            User(
                self.valid_username,
                self.valid_first_name,
                self.valid_last_name,
                "short",
                self.valid_role,
                self.valid_contact
            )

        with self.assertRaises(ValueError):
            User(
                self.valid_username,
                self.valid_first_name,
                self.valid_last_name,
                "longpassword" * 2,
                self.valid_role,
                self.valid_contact
            )

    def test_invalid_role(self):
        with self.assertRaises(ValueError):
            User(
                self.valid_username,
                self.valid_first_name,
                self.valid_last_name,
                self.valid_password,
                "invalid_role",
                self.valid_contact
            )

if __name__ == "__main__":
    unittest.main()