import unittest
from models.user import User
from models.roles import Roles
from commands.validation_helpers import (validate_first_name, validate_last_name, validate_username, 
                                         validate_password, role_validator, validate_contact)

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.valid_username = "test_user"
        self.valid_first_name = "John"
        self.valid_last_name = "Doe"
        self.valid_password = "password123"
        self.valid_role = Roles.WORKER.value
        self.valid_contact = "test@example.com"
    
    def test_valid_user_creation(self):
        user = User(self.valid_username, self.valid_first_name, self.valid_last_name, 
                    self.valid_password, self.valid_role, self.valid_contact)
        
        self.assertEqual(user.username, self.valid_username)
        self.assertEqual(user.first_name, self.valid_first_name)
        self.assertEqual(user.last_name, self.valid_last_name)
        self.assertEqual(user.password, self.valid_password)
        self.assertEqual(user.role, self.valid_role)
        self.assertEqual(user.contact, self.valid_contact)

    def test_invalid_first_name(self):
        with self.assertRaises(ValueError) as context:
            User(self.valid_username, "J", self.valid_last_name, 
                 self.valid_password, self.valid_role, self.valid_contact)
        self.assertEqual(str(context.exception), "First name has to be [2:15] characters long")

        with self.assertRaises(ValueError) as context:
            User(self.valid_username, "JohnJohnJohnJohn", self.valid_last_name, 
                 self.valid_password, self.valid_role, self.valid_contact)
        self.assertEqual(str(context.exception), "First name has to be [2:15] characters long")

    def test_invalid_last_name(self):
        with self.assertRaises(ValueError) as context:
            User(self.valid_username, self.valid_first_name, "D", 
                 self.valid_password, self.valid_role, self.valid_contact)
        self.assertEqual(str(context.exception), "Last name has to be [2:15] characters long")

        with self.assertRaises(ValueError) as context:
            User(self.valid_username, self.valid_first_name, "DoeDoeDoeDoeDoeDoe", 
                 self.valid_password, self.valid_role, self.valid_contact)
        self.assertEqual(str(context.exception), "Last name has to be [2:15] characters long")

    def test_invalid_username(self):
        with self.assertRaises(ValueError) as context:
            User("ab", self.valid_first_name, self.valid_last_name, 
                 self.valid_password, self.valid_role, self.valid_contact)
        self.assertEqual(str(context.exception), 'Username has to be [3:15] characters long')

        with self.assertRaises(ValueError) as context:
            User("a"*16, self.valid_first_name, self.valid_last_name, 
                 self.valid_password, self.valid_role, self.valid_contact)
        self.assertEqual(str(context.exception), 'Username has to be [3:15] characters long')

    def test_invalid_password(self):
        with self.assertRaises(ValueError) as context:
            User(self.valid_username, self.valid_first_name, self.valid_last_name, 
                 "short", self.valid_role, self.valid_contact)
        self.assertEqual(str(context.exception), 'Password has to be [8:15] characters long')

        with self.assertRaises(ValueError) as context:
            User(self.valid_username, self.valid_first_name, self.valid_last_name, 
                 "a"*16, self.valid_role, self.valid_contact)
        self.assertEqual(str(context.exception), 'Password has to be [8:15] characters long')

    def test_invalid_contact(self):
        with self.assertRaises(ValueError) as context:
            User(self.valid_username, self.valid_first_name, self.valid_last_name, 
                 self.valid_password, self.valid_role, "invalidemail.com")
        self.assertEqual(str(context.exception), "Enter your email address!")

    def test_invalid_role(self):
        with self.assertRaises(ValueError) as context:
            User(self.valid_username, self.valid_first_name, self.valid_last_name, 
                 self.valid_password, "NON_EXISTENT_ROLE", self.valid_contact)
        self.assertEqual(str(context.exception), "non existent role")
