import unittest
from commands.list_all_trucks import ListAllTrucks
from core.application_data import AppData

class TestListAllTrucks(unittest.TestCase):

    def setUp(self):
        self.app_data = AppData()
        self.app_data._create_trucks()

    def test_list_all_trucks(self):
        self.list_of_trucks = self.app_data.list_all_trucks()
        memo_len = len(self.list_of_trucks)
        for truck in self.list_of_trucks:
            self.assertEqual(len(self.list_of_trucks), memo_len)
            truck.mark_unavailable = 'Unavailable'
            memo_len -= 1


