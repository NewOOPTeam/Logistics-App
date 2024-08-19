import unittest
from unittest.mock import MagicMock
from commands.assign_truck_to_route import AssignTruckToRoute
from commands.constants.constants import OPERATION_CANCELLED, CANCEL, COMPLETED
from colorama import Fore


class AssignTruckToRouteTest(unittest.TestCase):

    def setUp(self):
        self.app_data = MagicMock()

        self.get_id = MagicMock()

        self.route = MagicMock()
        self.route._status = None
        self.route.total_distance = 100
        self.route.calculate_weight_at_start.return_value = 50

        self.truck = MagicMock()

        self.get_id.loop = MagicMock()
        self.get_id.loop.side_effect = [1, 2]

        self.app_data.get_route_by_id = MagicMock(return_value=self.route)
        self.app_data.find_suitable_truck = MagicMock(return_value=[self.truck])
        self.app_data.find_suitable_truck_by_weight = MagicMock(return_value=[self.truck])
        self.app_data.show_available_trucks = MagicMock(return_value="Available Trucks: Truck1")
        self.app_data.get_truck_by_id = MagicMock(return_value=self.truck)
        self.app_data.assign_truck_to_route = MagicMock(return_value="Assigned successfully")

        self.command = AssignTruckToRoute([], self.app_data)
        self.command._get_id = self.get_id

    def test_execute_successful(self):
        self.route._status = None

        result = self.command.execute()

        self.assertEqual(result, Fore.GREEN + "Assigned successfully")
        self.app_data.assign_truck_to_route.assert_called_once_with(self.truck, self.route)

    def test_execute_route_completed(self):
        self.route._status = COMPLETED

        with self.assertRaises(ValueError) as context:
            self.command.execute()

        self.assertEqual(str(context.exception), Fore.RED + "Cannot create delivery for a completed route.")

    def test_execute_no_suitable_trucks(self):
        self.app_data.find_suitable_truck = MagicMock(return_value=[])

        with self.assertRaises(ValueError) as context:
            self.command.execute()

        self.assertEqual(str(context.exception), Fore.RED + "No suitable truck available for this route distance.")

    def test_execute_no_suitable_trucks_by_weight(self):
        self.app_data.find_suitable_truck_by_weight = MagicMock(return_value=[])

        with self.assertRaises(ValueError) as context:
            self.command.execute()

        self.assertEqual(str(context.exception), Fore.RED + "No suitable truck available for package(s) weight.")

    def test_execute_cancelled(self):
        self.get_id.loop.side_effect = [CANCEL]

        result = self.command.execute()

        self.assertEqual(result, OPERATION_CANCELLED)

