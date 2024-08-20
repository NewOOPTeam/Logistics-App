import unittest
from unittest.mock import MagicMock
from models.courier_cost_calculator import CourierCostCalculator
from csv_file.distance_calculator import DistanceCalculator
from models.delivery_package import DeliveryPackage
from models.locations import Locations
from colorama import Fore

class TestCourierCostCalculator(unittest.TestCase):
    def setUp(self):
        self.mock_distance_calculator = MagicMock(spec=DistanceCalculator)
        self.cost_calculator = CourierCostCalculator(self.mock_distance_calculator)
        
        self.package = DeliveryPackage(
            weight=5.0,
            start_location=Locations.SYD,  
            end_location=Locations.MEL,    
            contact_info="Customer Info"
        )
    
    def test_calculateCostPositiveWeight_returnsCorrect(self):
        self.mock_distance_calculator.get_distance.return_value = 100.0
        
        base_cost = 10.0 + (2.00 * self.package.weight) + (0.075 * self.mock_distance_calculator.get_distance(self.package.start_location.name, self.package.end_location.name))
        insurance_cost = 0.05 * base_cost
        expected_cost = base_cost + insurance_cost
        
        result = self.cost_calculator.calculate_cost(self.package)
        
        self.assertAlmostEqual(result, expected_cost, places=2)
    
    def test_raisesValueError_when_CalculateCostNegativeDistance(self):
        self.mock_distance_calculator.get_distance.return_value = -100.0
        
        with self.assertRaises(ValueError):
            self.cost_calculator.calculate_cost(self.package)
    
    def test_calculateCostZeroDistance(self):
        self.mock_distance_calculator.get_distance.return_value = 0.0
        
        base_cost = 10.0 + (2.00 * self.package.weight) + (0.075 * self.mock_distance_calculator.get_distance(self.package.start_location.name, self.package.end_location.name))
        insurance_cost = 0.05 * base_cost
        expected_cost = base_cost + insurance_cost
        
        result = self.cost_calculator.calculate_cost(self.package)
        
        self.assertAlmostEqual(result, expected_cost, places=2)


