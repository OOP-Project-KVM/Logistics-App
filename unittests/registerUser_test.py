import unittest
from unittest.mock import Mock
from commands.register_user import RegisterUserCommand
from models.user import User
from core.application_data import ApplicationData

class TestRegisterUserCommand(unittest.TestCase):

    def setUp(self):
        self.app_data = Mock(spec=ApplicationData)
        self.valid_params = ["new_user", "Abcd", "Abc", "password123", "Worker", "test@example.com"]

        self.user = User(*self.valid_params)
        self.app_data.registrate_user.return_value = self.user

    def test_register_user_success(self):
        command = RegisterUserCommand(params=self.valid_params, app_data=self.app_data)
        result = command.execute()
        self.app_data.registrate_user.assert_called_once_with(*self.valid_params)
        self.app_data.login.assert_called_once_with(self.user)
        self.assertEqual(result, f"User with username: {self.valid_params[0]} registered successfully.")

    def test_register_user_already_exists(self):
        self.app_data.registrate_user.side_effect = ValueError(f"user with username:{self.valid_params[0]} already exists choose a different name!")
        command = RegisterUserCommand(params=self.valid_params, app_data=self.app_data)
        with self.assertRaises(ValueError) as context:
            command.execute()

        self.assertEqual(str(context.exception), f"user with username:{self.valid_params[0]} already exists choose a different name!")
        self.app_data.login.assert_not_called()

    def test_register_user_login(self):
        command = RegisterUserCommand(params=self.valid_params, app_data=self.app_data)
        command.execute()
        self.app_data.login.assert_called_once_with(self.user)
