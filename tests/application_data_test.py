import unittest
from models.user import User
from models.employee_roles import EmployeeRoles
from models.employee import Employee
from Vehicles.truck_class_model import TruckConstants as tc
from Vehicles.truck_class_model import TruckModel
from models.route_stop import RouteStop
from models.locations import Locations
from models.delivery_route import DeliveryRoute, COMPLETED
from date_time.date_time_functionalities import DateTime
from csv_file.distance_calculator import DistanceCalculator as DC
from colorama import Fore
from core.application_data import AppData
from models.delivery_package import DeliveryPackage, UNASSIGNED, ASSIGNED_TO_TRUCK, ASSIGNED_TO_ROUTE, IN_PROGRESS

class AppDataTests(unittest.TestCase):

    def setUp(self):
        self.app_data = AppData()
        self.date_time = DateTime()
        self.distance_calculator = DC()
        self.start_location = "SYD"
        self.end_location = "MEL"
        self.user = User("Ivan", "Ivan", "1234567890", "ivan@ivan")
        self.package = DeliveryPackage(weight=100, start_location=self.start_location, end_location=self.end_location, contact_info=self.user)

    def test_initialize_employees(self):
        self.assertEqual(len(self.app_data.employees), 4)

    def test_login_valid_employee(self):
        employee = self.app_data.find_employee_by_username("employee_user")
        self.app_data.login(employee)
        self.assertEqual(self.app_data.logged_in_employee, employee)

    def test_login_invalid_employee(self):
        employee = Employee("Invalid", "Employee", EmployeeRoles.EMPLOYEE, "invalid_user", "password123!")
        with self.assertRaises(ValueError):
            self.app_data.login(employee)

    def test_logout(self):
        employee = self.app_data.find_employee_by_username("employee_user")
        self.app_data.login(employee)
        self.app_data.logout()
        self.assertIsNone(self.app_data.logged_in_employee)

    def test_create_delivery_package(self):
        self.package = DeliveryPackage(weight=100, start_location=self.start_location, end_location=self.end_location, contact_info=self.user)
        package = self.app_data.create_delivery_package(100, (Locations.SYD.value, Locations.MEL.value), self.user)
        self.assertEqual(len(self.app_data.delivery_packages), 1)
        
        self.assertEqual(self.package.weight, 100)
        self.assertEqual(self.package.start_location, Locations.SYD)
        self.assertEqual(self.package.end_location, Locations.MEL)
        self.assertEqual(self.package._contact_info, self.user)
        self.assertEqual(self.package._id, 1) 


    def test_create_delivery_route(self):
        departure_time = self.date_time.date_from_string("Aug 19 2024 17:20h")
        route = self.app_data.create_delivery_route((Locations.SYD.value, Locations.MEL.value), departure_time)
        
        self.assertEqual(route.departure_time, departure_time)
        self.assertEqual(route.destinations[0].location, Locations.SYD.value)
        self.assertEqual(route.destinations[-1].location, Locations.MEL.value)

    def test_find_delivery_route(self):
        route1 = self.app_data.create_delivery_route((Locations.MEL.value, Locations.SYD.value), "10:00")
        route2 = self.app_data.create_delivery_route((Locations.SYD.value, Locations.BRI.value), "12:00")
        self.assertEqual(self.app_data.get_route_by_id(route1.id), route1)
        self.assertEqual(self.app_data.get_route_by_id(route2.id), route2)
        with self.assertRaises(ValueError):
            self.app_data.get_route_by_id(999)

    def test_findPackageByID_raisesValueError_whenNotExists(self):
        with self.assertRaises(ValueError):
            self.app_data.find_package_by_id(999)


    def test_view_packages(self):
        package1 = self.app_data.create_delivery_package(10, (Locations.SYD.value, Locations.MEL.value), User("John", "Doe", "1234567890", "john@example"))
        package2 = self.app_data.create_delivery_package(20, (Locations.BRI.value, Locations.PER.value), User("Jane", "Smith", "0987654321", "jane@example"))
        
        expected_output = f"{str(package1)}\n\n{str(package2)}"
        self.assertEqual(self.app_data.view_packages(), expected_output)

    def test_add_customer(self):
        customer = self.app_data.add_customer("John", "Doe", "1234567890", "john.doe@example.com")
        self.assertEqual(len(self.app_data.users), 1)
        self.assertEqual(customer.firstname, "John")
        self.assertEqual(customer.lastname, "Doe")
        self.assertEqual(customer.phone_number, "1234567890")
        self.assertEqual(customer.email, "john.doe@example.com")

    def test_find_customer_by_email(self):
        customer1 = self.app_data.add_customer("John", "Doe", "1234567890", "john.doe@example.com")
        customer2 = self.app_data.add_customer("Jane", "Smith", "0987654321", "jane.smith@example.com")
        self.assertEqual(self.app_data.find_customer_by_email(customer1.email), customer1)
        self.assertEqual(self.app_data.find_customer_by_email(customer2.email), customer2)
        with self.assertRaises(ValueError):
            self.app_data.find_customer_by_email("invalid@example.com")

   