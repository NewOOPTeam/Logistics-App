import unittest
from unittest.mock import MagicMock
from commands.create_delivery_route import CreateDeliveryRoute
from commands.constants.constants import OPERATION_CANCELLED, CANCEL
from colorama import Fore


class CreateDeliveryRouteTest(unittest.TestCase):

    def setUp(self):
        self.app_data = MagicMock()

        self.create_route = MagicMock()
        self.validate_departure_time = MagicMock()

        self.create_route.loop = MagicMock()
        self.create_route.loop.side_effect = ['Route Stops']

        self.validate_departure_time.loop = MagicMock()
        self.validate_departure_time.loop.side_effect = ['2024-08-20 08:00:00']

        self.delivery_route = MagicMock()
        self.delivery_route.__str__.return_value = 'Route Details'
        self.app_data.create_delivery_route = MagicMock(return_value=self.delivery_route)

        self.command = CreateDeliveryRoute([], self.app_data)
        self.command._get_route = self.create_route
        self.command._get_departure_time = self.validate_departure_time

    def test_execute_successful(self):
        result = self.command.execute()

        self.assertEqual(result, Fore.GREEN + 'Delivery route created: \nRoute Details')
        self.create_route.loop.assert_called_once()
        self.validate_departure_time.loop.assert_called_once()
        self.app_data.create_delivery_route.assert_called_once_with('Route Stops', '2024-08-20 08:00:00')

    def test_execute_cancelled_route(self):
        self.create_route.loop.side_effect = [CANCEL]

        result = self.command.execute()

        self.assertEqual(result, OPERATION_CANCELLED)

    def test_execute_cancelled_departure_time(self):
        self.create_route.loop.side_effect = ['Route Stops']
        self.validate_departure_time.loop.side_effect = [CANCEL]

        result = self.command.execute()

        # Verification
        self.assertEqual(result, OPERATION_CANCELLED)
