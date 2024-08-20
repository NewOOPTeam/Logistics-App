import unittest
from Vehicles.truck_class_model import TruckModel
from core.application_data import AppData

class TestTruckModel(unittest.TestCase):

    def setUp(self):
        self.truck = TruckModel(1001, 42000, 8000, "Scania")
        self.app_data = AppData()

    def test_truckId_returnsCorrect(self):
        self.assertEqual(self.truck.truck_id, 1001)

    def test_truckCapacity_returnsCorrect(self):
        self.assertEqual(self.truck.truck_capacity, 42000)

    def test_maxRange_returnsCorrect(self):
        self.assertEqual(self.truck.max_range, 8000)

    def test_status_returnsCorrect(self):
        self.assertEqual(self.truck.status, "Available")

    def test_name_returnsCorrect(self):
        self.assertEqual(self.truck.name, "Scania")
