import unittest
from csv_file.distance_calculator import DistanceCalculator
from models.delivery_package import DeliveryPackage
from models.courier_cost_calculator import CourierCostCalculator

class TestCourierCostCalculator(unittest.TestCase):
    def setUp(self):
        self.distance_calculator = DistanceCalculator()
        self.cost_calculator = CourierCostCalculator(self.distance_calculator)
        self.start_location = "SYD"
        self.end_location = "MEL"
        self.contact_info = "Customer Info"
        self.package = DeliveryPackage(weight=5.0, start_location=self.start_location, end_location=self.end_location, contact_info=self.contact_info)

    def test_calculate_cost_positive_weight(self):
        base_cost = 10.0 + (2.00 * self.package.weight) + (0.075 * self.distance_calculator.get_distance(self.start_location, self.end_location))
        insurance_cost = 0.05 * base_cost
        expected_cost = base_cost + insurance_cost
        self.assertEqual(self.cost_calculator.calculate_cost(self.package), expected_cost)

    def test_weight_setter_raises_error_for_zero_weight(self):
        with self.assertRaises(ValueError):
            self.package.weight = 0

    def test_weight_setter_raises_error_for_negative_weight(self):
        with self.assertRaises(ValueError):
            self.package.weight = -5.0

    def test_calculate_cost_negative_distance(self):
        self.distance_calculator.get_distance = lambda x, y: -100.0
        with self.assertRaises(ValueError):
            self.cost_calculator.calculate_cost(self.package)

if __name__ == "__main__":
    unittest.main()