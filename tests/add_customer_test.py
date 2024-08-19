import unittest
from commands.add_customer import AddCustomer
from commands.constants.constants import OPERATION_CANCELLED
from commands.login_command import LoginCommand
from core.application_data import AppData
from io import StringIO
import sys

from models.user import User


class TestAddCustomer(unittest.TestCase):
    def setUp(self):
        # Set up the necessary components for the test
        self.app_data = AppData()

        # Simulate logging in as an employee by providing login credentials
        sys.stdin = StringIO('employee_user\npassword123!\n')
        login_command = LoginCommand([], self.app_data)
        login_command.execute()

    def test_add_customer_successful(self):
        sys.stdin = StringIO('Ivan\nIvan\nivan@ivan\n099999999\n')

        command = AddCustomer([], self.app_data)
        result = command.execute()

        self.assertIn('User Ivan Ivan added', result)
        self.assertEqual(len(self.app_data._users), 1)
        self.assertEqual(self.app_data._users[0].firstname, 'Ivan')
        self.assertEqual(self.app_data._users[0].lastname, 'Ivan')
        self.assertEqual(self.app_data._users[0].email, 'ivan@ivan')
        self.assertEqual(self.app_data._users[0].phone_number, '099999999')

    def test_returnsCorrect_whenNameIsCorrect(self):
        customer = self.app_data.add_customer('Ivan', 'Ivan', '099999999', 'ivan@ivan')
        self.assertEqual(len(self.app_data._users), 1)

    def test_raiseValueError_whenNameIsNotCorrect(self):
        with self.assertRaises(ValueError):
            customer = self.app_data.add_customer('iv', 'iv', '099999999', 'ivan@ivan')

    def test_returnsCorrect_whenEmailIsCorrect(self):
        customer = self.app_data.add_customer('Ivan', 'Ivan', '099999999', 'ivan@ivan')
        self.assertEqual((self.app_data._users[0].email), 'ivan@ivan')
    
    def test_raiseValueError_whenEmailIsNotCorrect(self):
        with self.assertRaises(ValueError):
            customer = self.app_data.add_customer('Ivan', 'Ivan', '099999999', 'ivanivan')

    def test_returnsCorrect_whenPhoneIsCorrect(self):
        customer = self.app_data.add_customer('Ivan', 'Ivan', '099999999', 'ivan@ivan')
        self.assertEqual((self.app_data._users[0].phone_number), '099999999')
    
    def test_raiseValueError_whenPhoneIsNotCorrect(self):
        with self.assertRaises(ValueError):
            customer = self.app_data.add_customer('Ivan', 'Ivan', '099999', 'ivan@ivan')