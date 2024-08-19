import unittest
from unittest.mock import MagicMock
from commands.add_customer import AddCustomer
from commands.constants.constants import *


class TestAddCustomer(unittest.TestCase):

    def test_execute_successful(self):
        app_data = MagicMock()
        mock_get_name = MagicMock()
        mock_get_email = MagicMock()
        mock_get_phone = MagicMock()

        mock_get_name.loop.side_effect = ['John', 'Doe']
        mock_get_email.loop.return_value = 'john.doe@example.com'
        mock_get_phone.loop.return_value = '1234567890'

        # Create an AddCustomer instance and inject the mocks
        command = AddCustomer([], app_data)
        command._get_customer_name = mock_get_name
        command._get_email = mock_get_email
        command._get_phone = mock_get_phone

        mock_customer = MagicMock()
        mock_customer.firstname = 'John'
        mock_customer.lastname = 'Doe'
        app_data.add_customer.return_value = mock_customer

        result = command.execute()

        self.assertEqual(result, 'User John Doe added')
        app_data.add_customer.assert_called_once_with('John', 'Doe', '123-456-7890', 'john.doe@example.com')

    def test_execute_cancelled(self):

        app_data = MagicMock()
        mock_get_name = MagicMock()
        mock_get_email = MagicMock()
        mock_get_phone = MagicMock()

        mock_get_name.loop.side_effect = [CANCEL]
        command = AddCustomer([], app_data)
        command._get_customer_name = mock_get_name
        command._get_email = mock_get_email
        command._get_phone = mock_get_phone

        result = command.execute()

        self.assertEqual(result, OPERATION_CANCELLED)

