import unittest
from unittest.mock import Mock
from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.logout_user import LogoutUserCommand

class TestLogoutUserCommand(unittest.TestCase):
    
    def setUp(self):
        self.app_data = Mock(ApplicationData)
        self.command = LogoutUserCommand(params=[], app_data=self.app_data)

    def test_execute_calls_logout(self):
        result = self.command.execute()
        self.app_data.logout.assert_called_once()
        self.assertEqual(result, "You logged out!")

    def test_logout_effect(self):
        self.app_data.logout.side_effect = lambda: setattr(self.app_data, '_logged_user', None)
        self.command.execute()
        self.assertIsNone(self.app_data._logged_user)