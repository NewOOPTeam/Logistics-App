import unittest
from csv_file.distance_calculator import DistanceCalculator
from pathlib import Path
from colorama import Fore

class TestDistanceCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = DistanceCalculator()

    def test_load_distance_data(self):
        distance_dict = self.calculator.load_distance_data()
        self.assertIsInstance(distance_dict, dict)
        self.assertEqual(len(distance_dict), 7)  # Updated to match the actual number of cities
        self.assertIn('SYD', distance_dict)
        self.assertIn('MEL', distance_dict)
        self.assertIn('ADL', distance_dict)
        self.assertIn('ASP', distance_dict)
        self.assertIn('BRI', distance_dict)
        self.assertIn('DAR', distance_dict)
        self.assertIn('PER', distance_dict)
        self.assertEqual(distance_dict['SYD']['MEL'], 877)
        self.assertEqual(distance_dict['SYD']['ADL'], 1376)
        self.assertEqual(distance_dict['SYD']['ASP'], 2762)
        self.assertEqual(distance_dict['MEL']['ADL'], 725)
        self.assertEqual(distance_dict['MEL']['ASP'], 2255)
        self.assertEqual(distance_dict['ADL']['ASP'], 1530)

    def test_get_distance(self):
        distance = self.calculator.get_distance('SYD', 'MEL')
        self.assertEqual(distance, 877)

        distance = self.calculator.get_distance('MEL', 'ADL')
        self.assertEqual(distance, 725)

        with self.assertRaises(ValueError):
            self.calculator.get_distance('SYD', 'XYZ')

    def test_calculate_total_distance(self):
        route = ['SYD', 'MEL', 'ADL']
        total_distance = self.calculator.calculate_total_distance(route)
        self.assertEqual(total_distance, 877 + 725)

        route = ['SYD', 'ASP', 'PER']
        total_distance = self.calculator.calculate_total_distance(route)
        self.assertEqual(total_distance, 2762 + 2481)

    def test_validate_route(self):
        route = ['SYD', 'MEL', 'ADL']
        self.calculator.validate_route(route)

        route = ['SYD', 'MEL', 'MEL']
        with self.assertRaises(ValueError):
            self.calculator.validate_route(route)

        route = ['SYD']
        with self.assertRaises(ValueError):
            self.calculator.validate_route(route)

        route = ['SYD', 'XYZ']
        with self.assertRaises(ValueError):
            self.calculator.validate_route(route)

    def test_get_route_distance(self):
        route_input = 'SYD MEL ADL'
        distance = self.calculator.get_route_distance(route_input)
        self.assertEqual(distance, 877 + 725)

        route_input = 'SYD ASP PER'
        distance = self.calculator.get_route_distance(route_input)
        self.assertEqual(distance, 2762 + 2481)

        route_input = 'SYD MEL MEL'
        with self.assertRaises(ValueError):
            self.calculator.get_route_distance(route_input)
