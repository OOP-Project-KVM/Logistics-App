import unittest
from unittest.mock import Mock
from commands.search_route import SearchRouteCommand
from core.application_data import ApplicationData
from models.route import Route
from models.location import Location

class TestSearchRouteCommand(unittest.TestCase):

    def setUp(self):
        self.app_data = Mock(ApplicationData)

        loc1 = Location(name="SYD")
        loc2 = Location(name="MEL")
        route1 = Route(id=1, locations=[loc1, loc2])
        self.app_data._routes = [route1]
        self.params = ["SYD", "MEL"]

    def test_search_route_success(self):
        self.app_data.search_route.return_value = "Route found."
        command = SearchRouteCommand(params=self.params, app_data=self.app_data)
        result = command.execute()
        self.assertEqual(result, "Route found.")

    def test_search_route_no_match(self):
        self.app_data.search_route.return_value = "No routes found."
        command = SearchRouteCommand(params=["UNKNOWN", "END"], app_data=self.app_data)
        result = command.execute()
        self.assertEqual(result, "No routes found.")

    def test_search_route_case_insensitivity(self):
        self.app_data.search_route.return_value = "Route found."
        command = SearchRouteCommand(params=["start", "end"], app_data=self.app_data)
        result = command.execute()
        self.assertEqual(result, "Route found.")
