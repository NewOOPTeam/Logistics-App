import unittest
from unittest.mock import MagicMock, patch
from commands.view_routes_in_progress import ViewRoutesInProgress
from core.application_data import AppData
from models.employee_roles import EmployeeRoles
from colorama import Fore

class TestViewRoutesInProgress(unittest.TestCase):

    def setUp(self):
        self.app_data = MagicMock(spec=AppData)

        self.mock_employee = MagicMock()
        self.app_data.logged_in_employee = self.mock_employee

        self.mock_route_1 = MagicMock()
        self.mock_route_1._status = 'In progress'
        self.mock_route_1.__str__.return_value = "Route 1: Details"
        
        self.mock_route_2 = MagicMock()
        self.mock_route_2._status = 'In progress'
        self.mock_route_2.__str__.return_value = "Route 2: Details"
        
        self.mock_route_3 = MagicMock()
        self.mock_route_3._status = 'Completed'
        self.mock_route_3.__str__.return_value = "Route 3: Details"

    def test_execute_success(self):
        self.mock_employee.role = EmployeeRoles.MANAGER

        self.app_data.get_routes_in_progress.return_value = [
            str(self.mock_route_1),
            str(self.mock_route_2)
        ]

        command = ViewRoutesInProgress([], self.app_data)
        result = command.execute()

        self.app_data.get_routes_in_progress.assert_called_once()

        expected_output = "Route 1: Details\nRoute 2: Details"
        self.assertEqual(result, expected_output)

    def test_execute_fail_not_manager(self):
        self.mock_employee.role = EmployeeRoles.SUPERVISOR

        command = ViewRoutesInProgress([], self.app_data)
        with self.assertRaises(ValueError):
            command.execute()

    @patch('commands.view_routes_in_progress.AppData', autospec=True)
    
    def test_execute_no_routes_in_progress(self, app_data_class_mock):
        self.mock_employee.role = EmployeeRoles.MANAGER

        app_data_mock = app_data_class_mock.return_value
        app_data_mock.get_routes_in_progress.return_value = []

        command = ViewRoutesInProgress([], self.app_data)
        
        result = command.execute()

        self.assertEqual(result, '')

