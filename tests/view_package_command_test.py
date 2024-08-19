import unittest
from unittest.mock import MagicMock, patch
from commands.view_package import ViewPackage
from core.application_data import AppData
from commands.interaction_loops.get_id import GetId
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from models.delivery_package import DeliveryPackage, ASSIGNED_TO_TRUCK, COMPLETED
from models.locations import Locations
from models.user import User
from colorama import Fore

class TestViewPackage(unittest.TestCase):

    def setUp(self):
        self.app_data = MagicMock(spec=AppData)

        self.get_id_mock = MagicMock(spec=GetId)

        self.date_time_mock = MagicMock()

        self.mock_user = MagicMock(spec=User)
        self.mock_user.__str__.return_value = "Ivan Ivan, 099-999-999"
        
        self.mock_package = MagicMock(spec=DeliveryPackage)
        self.mock_package.id = 1
        self.mock_package.weight = 5.0
        self.mock_package.start_location = Locations.SYD
        self.mock_package.end_location = Locations.MEL
        self.mock_package.status = ASSIGNED_TO_TRUCK
        self.mock_package._contact_info = self.mock_user
        self.mock_package.arrival_time = 'Aug 19 2024 17:20h'
        self.mock_package.__str__.return_value = (
            Fore.LIGHTCYAN_EX + '#1 Package (' + Fore.YELLOW + '5.0kg' + Fore.LIGHTCYAN_EX + ')\n'
            'From: ' + Fore.YELLOW + Locations.SYD.value + Fore.LIGHTCYAN_EX + '\n'
            'To: ' + Fore.YELLOW + Locations.MEL.value + Fore.LIGHTCYAN_EX + '\n'
            '-----Client-----\n'
            'Ivan Ivan, 099-999-999\n'
            '----------------\n'
            'STATUS: In progress\n'
            'Expected delivery: Aug 19 2024 17:20h'
        )

        self.app_data.find_package_by_id.return_value = self.mock_package
        self.date_time_mock.create_time_stamp_for_today.return_value = 'Aug 19 2024 17:20h'

    @patch('commands.view_package.DateTime', autospec=True)
    @patch('commands.view_package.GetId', autospec=True)
    def test_execute_success(self, get_id_mock, date_time_mock):

        get_id_mock.return_value = self.get_id_mock
        self.get_id_mock.loop.return_value = 1

        date_time_mock.create_time_stamp_for_today.return_value = 'Aug 19 2024 17:20h'

        command = ViewPackage([], self.app_data)
        result = command.execute()

        self.app_data.find_package_by_id.assert_called_with(1)

        self.mock_package.update_status.assert_called_with('Aug 19 2024 17:20h')

        expected_str = (
            Fore.LIGHTCYAN_EX + '#1 Package (' + Fore.YELLOW + '5.0kg' + Fore.LIGHTCYAN_EX + ')\n'
            'From: ' + Fore.YELLOW + Locations.SYD.value + Fore.LIGHTCYAN_EX + '\n'
            'To: ' + Fore.YELLOW + Locations.MEL.value + Fore.LIGHTCYAN_EX + '\n'
            '-----Client-----\n'
            'Ivan Ivan, 099-999-999\n'
            '----------------\n'
            'STATUS: In progress\n'
            'Expected delivery: Aug 19 2024 17:20h'
        )
        self.assertEqual(result, expected_str)

    @patch('commands.view_package.GetId', autospec=True)
    def test_execute_cancel(self, get_id_mock):
        get_id_mock.return_value = self.get_id_mock
        self.get_id_mock.loop.return_value = CANCEL

        command = ViewPackage([], self.app_data)
        result = command.execute()

        self.assertEqual(result, OPERATION_CANCELLED)

    def tearDown(self):
        pass


