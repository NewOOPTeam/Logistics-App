import unittest
from unittest.mock import MagicMock
from commands.view_all_packages import ViewAllPackages
from core.application_data import AppData
from models.employee_roles import EmployeeRoles
from colorama import Fore

class TestViewAllPackages(unittest.TestCase):

    def setUp(self):
        self.app_data = MagicMock(spec=AppData)

        self.supervisor_employee = MagicMock()
        self.supervisor_employee.role = EmployeeRoles.SUPERVISOR
        self.app_data.logged_in_employee = self.supervisor_employee

        self.mock_packages = "Package 1 details\n\nPackage 2 details\n\nPackage 3 details"
        self.app_data.view_packages.return_value = self.mock_packages

    def test_initialization(self):
        command = ViewAllPackages([], self.app_data)
        self.assertIsInstance(command, ViewAllPackages)
        self.assertEqual(command._app_data, self.app_data)

    def test_execute_non_supervisor(self):
        self.app_data.logged_in_employee.role = EmployeeRoles.EMPLOYEE

        command = ViewAllPackages([], self.app_data)
        with self.assertRaises(ValueError) as context:
            command.execute()
        self.assertEqual(str(context.exception), Fore.RED + 'Only supervisors can view all packages!')

    def test_execute_success(self):
        self.app_data.logged_in_employee.role = EmployeeRoles.SUPERVISOR

        command = ViewAllPackages([], self.app_data)
        result = command.execute()
        self.assertEqual(result, self.mock_packages)

