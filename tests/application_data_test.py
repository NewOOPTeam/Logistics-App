import unittest
from unittest.mock import MagicMock, patch
from models.delivery_package import DeliveryPackage, UNASSIGNED, ASSIGNED_TO_TRUCK, ASSIGNED_TO_ROUTE, IN_PROGRESS
from models.user import User
from models.employee_roles import EmployeeRoles
from models.employee import Employee
from Vehicles.truck_class_model import TruckModel
from models.route_stop import RouteStop
from models.locations import Locations
from models.delivery_route import DeliveryRoute, COMPLETED
from csv_file.distance_calculator import DistanceCalculator as DC
from core.application_data import AppData

class TestAppData(unittest.TestCase):
    
    def setUp(self):
        self.app_data = AppData()
        self.mock_distance_calculator = MagicMock(spec=DC)
        self.app_data._distance_calculator = self.mock_distance_calculator  
    
    def test_initialize_employees(self):
        self.assertEqual(len(self.app_data.employees), 4)
        self.assertEqual(self.app_data.employees[0].username, 'employee_user')
        self.assertEqual(self.app_data.employees[1].role, EmployeeRoles.SUPERVISOR)
    
    def test_create_trucks(self):
        self.assertEqual(len(self.app_data.trucks), 40)
        scania_trucks = [truck for truck in self.app_data.trucks if truck.name == 'Scania']
        self.assertEqual(len(scania_trucks), 10)
    
    def test_find_employee_by_username(self):
        employee = self.app_data.find_employee_by_username('employee_user')
        self.assertIsNotNone(employee)
        self.assertEqual(employee.username, 'employee_user')
    
    def test_login(self):
        employee = self.app_data.find_employee_by_username('employee_user')
        self.app_data.login(employee)
        self.assertTrue(self.app_data.has_logged_in_employee)
        self.assertEqual(self.app_data.logged_in_employee, employee)
    
    def test_login_failure(self):
        employee = Employee("Non", "Existent", EmployeeRoles.EMPLOYEE, "nonexistent_user", "password")
        with self.assertRaises(ValueError):
            self.app_data.login(employee)
    
    def test_logout(self):
        employee = self.app_data.find_employee_by_username('employee_user')
        self.app_data.login(employee)
        self.app_data.logout()
        self.assertFalse(self.app_data.has_logged_in_employee)
    
    def test_add_customer(self):
        user = self.app_data.add_customer('John', 'Doe', '+1234567890', 'john.doe@example.com')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'john.doe@example.com')
    
    def test_find_customer_by_email(self):
        user = self.app_data.add_customer('Jane', 'Doe', '+1234567890', 'jane.doe@example.com')
        found_user = self.app_data.find_customer_by_email('jane.doe@example.com')
        self.assertEqual(user, found_user)
    
    def test_create_delivery_package(self):
        user = self.app_data.add_customer('Alice', 'Smith', '+1234567890', 'alice.smith@example.com')
        package = self.app_data.create_delivery_package(10.0, (Locations.SYD.name, Locations.MEL.name), user)
        self.assertIsInstance(package, DeliveryPackage)
        self.assertEqual(package.start_location, Locations.SYD)
        self.assertEqual(package.end_location, Locations.MEL)
    
    def test_find_package_by_id(self):
        user = self.app_data.add_customer('Bob', 'Brown', '+1234567890', 'bob.brown@example.com')
        package = self.app_data.create_delivery_package(15.0, (Locations.ADL.name, Locations.BRI.name), user)
        found_package = self.app_data.find_package_by_id(package.id)
        self.assertEqual(package, found_package)
    
    def test_view_packages(self):
        user = self.app_data.add_customer('Chris', 'Green', '+1234567890', 'chris.green@example.com')
        self.app_data.create_delivery_package(20.0, (Locations.DAR.name, Locations.PER.name), user)
        view_output = self.app_data.view_packages()
        self.assertIn('Chris Green', view_output)
    
    def test_get_package_locations(self):
        user = self.app_data.add_customer('Dana', 'White', '+1234567890', 'dana.white@example.com')
        package = self.app_data.create_delivery_package(25.0, (Locations.SYD.name, Locations.MEL.name), user)
        start_location, end_location = self.app_data.get_package_locations(package.id)
        self.assertEqual(start_location, Locations.SYD)
        self.assertEqual(end_location, Locations.MEL)
    
    def test_create_delivery_route(self):
        self.mock_distance_calculator.calculate_total_distance.return_value = 500
        route = self.app_data.create_delivery_route((Locations.SYD.name, Locations.MEL.name), 'Aug 20 2024 17:20h')
        self.assertIsInstance(route, DeliveryRoute)
        self.assertEqual(len(route.destinations), 2)

    
    def test_get_route_by_id(self):
        self.mock_distance_calculator.calculate_total_distance.return_value = 500
        route = self.app_data.create_delivery_route((Locations.SYD.name, Locations.MEL.name), 'Aug 20 2024 17:20h')
        found_route = self.app_data.get_route_by_id(route.id)
        self.assertEqual(route, found_route)
    
    def test_find_valid_routes_for_package(self):
        self.mock_distance_calculator.calculate_total_distance.return_value = 500
        user = self.app_data.add_customer('Eve', 'Black', '+1234567890', 'eve.black@example.com')
        package = self.app_data.create_delivery_package(30.0, (Locations.ASP.name, Locations.PER.name), user)
        route = self.app_data.create_delivery_route((Locations.ASP.name, Locations.PER.name), 'Aug 20 2024 17:20h')
        valid_routes = self.app_data.find_valid_routes_for_package(package)
        self.assertIn(route, valid_routes)
    
    def test_assign_package_to_route(self):
        self.mock_distance_calculator.calculate_total_distance.return_value = 500
        user = self.app_data.add_customer('Frank', 'Blue', '+1234567890', 'frank.blue@example.com')
        package = self.app_data.create_delivery_package(35.0, (Locations.SYD.name, Locations.MEL.name), user)
        route = self.app_data.create_delivery_route((Locations.SYD.name, Locations.MEL.name), 'Aug 20 2024 17:20h')
        assigned_package = self.app_data.assign_package_to_route(package.id, route.id)
        self.assertEqual(assigned_package.status, ASSIGNED_TO_ROUTE)
    
    def test_assign_truck_to_route(self):
        user = self.app_data.add_customer('Grace', 'Red', '+1234567890', 'grace.red@example.com')
        package = self.app_data.create_delivery_package(40.0, (Locations.SYD.name, Locations.MEL.name), user)
        route = self.app_data.create_delivery_route((Locations.SYD.name, Locations.MEL.name), 'Aug 20 2024 17:20h')
        truck = TruckModel(1, 100, 1000, 'Scania')
        self.app_data._trucks.append(truck)
    
        route._packages.append(package)  
    
        result = self.app_data.assign_truck_to_route(truck, route)
        
        self.assertIn(package, truck._packages)
        
    def test_find_suitable_truck_by_distance(self):
        truck = TruckModel(2, 150, 1500, 'Man')
        self.app_data._trucks.append(truck)
        suitable_trucks = self.app_data.find_suitable_truck_by_distance(1000)
        self.assertIn(truck, suitable_trucks)

