import unittest
from core.application_data import AppData
from commands.add_customer import AddCustomer

class TestAddCustomer(unittest.TestCase):
    def setUp(self):
        self.app_data = AppData()
        self.command = AddCustomer(["John", "Doe", "1234567890", "john.doe@example.com"], self.app_data)

    def test_execute(self):
        result = self.command.execute()
        self.assertEqual(result, "User John Doe added")


if __name__ == "__main__":
    unittest.main()
