import unittest
from unittest.mock import MagicMock
from commands.create_package import CreatePackage
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from colorama import Fore

class CreatePackageTest(unittest.TestCase):

    def setUp(self):
        # Mock AppData instance
        self.app_data = MagicMock()

        # Mock interaction loops
        self.get_weight = MagicMock()
        self.get_start_end_location = MagicMock()
        self.get_customer_info = MagicMock()
        self.create_route = MagicMock()
        self.validate_departure_time = MagicMock()
        self.get_id = MagicMock()

        # Mock route and package objects
        self.route = ('start', 'end')
        self.package = MagicMock()
        self.package.id = 1
        self.new_route = MagicMock()
        self.new_route.id = 2

        # Mock the methods for creating and assigning packages
        self.app_data.create_delivery_package = MagicMock(return_value=self.package)
        self.app_data.find_valid_routes_for_package = MagicMock(return_value=[self.new_route])
        self.app_data.get_route_by_id = MagicMock(return_value=self.new_route)
        self.app_data.assign_package_to_route = MagicMock(return_value=self.package)
        self.app_data.create_delivery_route = MagicMock(return_value=self.new_route)

        # Set up common mock behaviors
        self.get_weight.loop = MagicMock(return_value=10)
        self.get_start_end_location.loop = MagicMock(return_value=self.route)
        self.get_customer_info.loop = MagicMock(return_value='customer@example.com')
        self.create_route.loop = MagicMock(return_value=self.route)
        self.validate_departure_time.loop = MagicMock(return_value='2024-08-20 08:00:00')
        self.get_id.loop = MagicMock(return_value=self.new_route.id)

        # Create the command instance with mocked dependencies
        self.command = CreatePackage([], self.app_data)
        self.command._get_weight = self.get_weight
        self.command._get_start_end_location = self.get_start_end_location
        self.command._get_customer_info = self.get_customer_info
        self.command._create_route = self.create_route
        self.command._validate_departure_time = self.validate_departure_time
        self.command._get_id = self.get_id

    def test_execute_successful(self):
        # Simulate a successful package creation and assignment to route
        result = self.command.execute()

        # Verification
        expected_message = (
            f'{Fore.GREEN}Delivery created for Package #{Fore.YELLOW}{self.package.id}{Fore.GREEN}, '
            f'assigned to route #{Fore.YELLOW}{self.new_route.id}{Fore.GREEN}:\n{Fore.RESET}'
            f'\n{self.new_route}\n\n'
            f'{Fore.YELLOW}Awaiting assignment to available truck.{Fore.RESET}'
        )
        self.assertEqual(result, expected_message)
        self.app_data.create_delivery_package.assert_called_once_with(10, self.route, 'customer@example.com')
        self.app_data.find_valid_routes_for_package.assert_called_once_with(self.package.id)
        self.app_data.assign_package_to_route.assert_called_once_with(self.package.id, self.new_route.id)

    def test_execute_no_valid_routes(self):
        # Simulate no valid routes
        self.app_data.find_valid_routes_for_package = MagicMock(return_value=[])

        result = self.command.execute()

        # Verification
        self.assertEqual(result, OPERATION_CANCELLED)
        self.app_data.create_delivery_route.assert_called_once()
        self.app_data.create_delivery_route.assert_called_with(self.route, '2024-08-20 08:00:00')

    def test_execute_cancelled_weight(self):
        # Simulate cancellation in weight input
        self.get_weight.loop = MagicMock(return_value=CANCEL)

        result = self.command.execute()

        # Verification
        self.assertEqual(result, OPERATION_CANCELLED)
        self.app_data.create_delivery_package.assert_not_called()

    def test_execute_cancelled_route(self):
        # Simulate cancellation in route input
        self.get_start_end_location.loop = MagicMock(return_value=CANCEL)

        result = self.command.execute()

        # Verification
        self.assertEqual(result, OPERATION_CANCELLED)
        self.app_data.create_delivery_package.assert_not_called()

    def test_execute_cancelled_customer(self):
        # Simulate cancellation in customer email input
        self.get_customer_info.loop = MagicMock(return_value=CANCEL)

        result = self.command.execute()

        # Verification
        self.assertEqual(result, OPERATION_CANCELLED)
        self.app_data.create_delivery_package.assert_not_called()

    def test_validate_route_invalid_route(self):
        # Simulate an invalid route during validation
        invalid_route = ('wrong_start', 'wrong_end')
        self.create_route.loop = MagicMock(return_value=invalid_route)

        with self.assertRaises(ValueError):
            self.command.validate_route(self.route, invalid_route)

    def test_validate_route_successful(self):
        # Simulate a valid route
        valid_route = ('start', 'end')
        result = self.command.validate_route(self.route, valid_route)

        self.assertEqual(result, valid_route)

