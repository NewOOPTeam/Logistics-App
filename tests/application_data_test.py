import unittest
from models.user import User
from models.employee_roles import EmployeeRoles
from models.employee import Employee
from Vehicles.truck_class_model import TruckConstants, TruckModel
from models.locations import Locations
from core.application_data import AppData
from date_time.date_time_functionalities import DateTime
from models.delivery_package import DeliveryPackage
from models.locations import Locations



class AppDataTests(unittest.TestCase):

    def setUp(self):
        self.app_data = AppData()
        self.date_time = DateTime()
        self.app_data.initialize_employees()
<<<<<<< HEAD

=======
>>>>>>> origin/main

    def test_initialize_employees(self):
        self.app_data.initialize_employees()
        self.assertEqual(len(self.app_data.employees), 4)

    def test_login_valid_employee(self):
        employee = self.app_data.find_employee_by_username("employee_user")
        self.app_data.login(employee)
        self.assertEqual(self.app_data.logged_in_employee, employee)
<<<<<<< HEAD

=======
>>>>>>> origin/main

    def test_login_invalid_employee(self):
        employee = Employee("Invalid", "Employee", EmployeeRoles.EMPLOYEE, "invalid_user", "password123!")
        self.app_data.initialize_employees()
        with self.assertRaises(ValueError):
            self.app_data.login(employee)

    def test_logout(self):
        employee = self.app_data.find_employee_by_username("employee_user")
        self.app_data.login(employee)
        self.app_data.logout()
 
    def test_create_delivery_package(self):
        user = User("John", "Doe", "1234567890", "john.doe@example.com")
        package = self.app_data.create_delivery_package(10, Locations.SYD.value, Locations.MEL.value, user)
        self.assertEqual(len(self.app_data.delivery_packages), 1)
        self.assertEqual(package.weight, 10)
        self.assertEqual(package._start_location, Locations.SYD.value)
        self.assertEqual(package._end_location, Locations.MEL.value)
        self.assertEqual(package._contact_info, user)

    def test_create_delivery_route(self):
        departure_time = self.date_time.date_from_string("10/10/23")
        arrival_time = self.date_time.date_from_string("12/10/23")
        route = self.app_data.create_delivery_route(departure_time, arrival_time, Locations.SYD.value, Locations.MEL.value)
        
        self.assertEqual(route.departure_time, departure_time)
        self.assertEqual(route.arrival_time, arrival_time)
        self.assertEqual(route.starting_location, Locations.SYD.value)
        self.assertEqual(route.final_location, Locations.MEL.value)

    def test_find_delivery_route(self):
        route1 = self.app_data.create_delivery_route("10:00", "12:00", Locations.SYD.value, Locations.MEL.value)
        route2 = self.app_data.create_delivery_route("12:00", "14:00", Locations.MEL.value, Locations.BRI.value)
        route3 = self.app_data.create_delivery_route("14:00", "16:00", Locations.ADL.value, Locations.PER.value)
        self.assertEqual(self.app_data.find_delivery_route(Locations.SYD.value, Locations.MEL.value), (route1,))
        self.assertEqual(self.app_data.find_delivery_route(Locations.MEL.value, Locations.BRI.value), (route2,))
        self.assertEqual(self.app_data.find_delivery_route(Locations.ADL.value, Locations.PER.value), (route3,))
        self.assertEqual(self.app_data.find_delivery_route("SOF", Locations.PER), "Invalid start or end point: SOF, Locations.PER")
    
    def test_find_package_by_id(self):
        package1 = self.app_data.create_delivery_package(10, Locations.SYD, Locations.MEL, User("John", "Doe", "1234567890", "john.doe@example.com"))
        package2 = self.app_data.create_delivery_package(20, Locations.BRI, Locations.PER, User("Jane", "Smith", "0987654321", "jane.smith@example.com"))
        
        self.assertEqual(self.app_data.find_package_by_id(package1.id), package1)
        self.assertEqual(self.app_data.find_package_by_id(package2.id), package2)
        
        with self.assertRaises(ValueError):
            self.app_data.find_package_by_id(999)

    def test_view_packages(self):
        package1 = self.app_data.create_delivery_package(10, Locations.SYD, Locations.MEL, User("John", "Doe", "1234567890", "john.doe@example.com"))
        package2 = self.app_data.create_delivery_package(20, Locations.BRI, Locations.PER, User("Jane", "Smith", "0987654321", "jane.smith@example.com"))
        
        expected_output = f"{str(package1)}\n{str(package2)}"
        self.assertEqual(self.app_data.view_packages(), expected_output)

    def test_view_employees(self):
        self.app_data.initialize_employees()
        
        expected_output = (
            "Employee EmployeeLast, Role: EmployeeRoles.EMPLOYEE, Username: employee_user\n"
            "Supervisor SupervisorLast, Role: EmployeeRoles.SUPERVISOR, Username: supervisor_user\n"
            "Manager ManagerLast, Role: EmployeeRoles.MANAGER, Username: manager_user\n"
            "Admin AdminLast, Role: EmployeeRoles.ADMIN, Username: admin_user"
        )
        
        actual_output = self.app_data.view_employees()
        
        self.assertEqual(actual_output, expected_output)
    
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

    def test_add_employee(self):
        employee = self.app_data.add_employee("Employee", "EmployeeLast", EmployeeRoles.EMPLOYEE, "employee_user", "password123!")
        
        self.assertEqual(len(self.app_data.employees), 1)
        self.assertEqual(employee.firstname, "Employee")
        self.assertEqual(employee.lastname, "EmployeeLast")
        self.assertEqual(employee.role, EmployeeRoles.EMPLOYEE)
        self.assertEqual(employee.username, "employee_user")
        self.assertEqual(employee.password, "password123!")

    def test_get_truck_by_id(self):
        truck1 = TruckModel(1001, TruckConstants.SCANIA_CAPACITY, TruckConstants.SCANIA_MAX_RANGE, "Scania")
        truck2 = TruckModel(1011, TruckConstants.MAN_CAPACITY, TruckConstants.MAN_MAX_RANGE, "Man")
        self.app_data._trucks = [truck1, truck2]
        self.assertEqual(self.app_data.get_truck_by_id(1001), truck1)
        self.assertEqual(self.app_data.get_truck_by_id(1011), truck2)
        with self.assertRaises(ValueError):
            self.app_data.get_truck_by_id(9999)

    def test_assign_package_to_delivery_route(self):
        package = self.app_data.create_delivery_package(2000, Locations.MEL.value, Locations.SYD.value, User("John", "Doe", "1234567890", "john.doe@example.com"))
        route = self.app_data.create_delivery_route("10:00", "12:00", Locations.ADL.value, Locations.MEL.value, Locations.SYD.value)
        self.app_data.assign_package_to_delivery_route(package.id, route.id)
        self.assertEqual(route.packages, (package,)) 

    def test_find_suitable_truck(self):
        truck1 = TruckModel(1005, 1000, 100, "Scania")
        truck2 = TruckModel(1016, 2000, 200, "Man")
        self.app_data._trucks = [truck1, truck2]
        self.assertEqual(self.app_data.find_suitable_truck(500, 50), truck1)
        self.assertEqual(self.app_data.find_suitable_truck(1500, 150), truck2)
        with self.assertRaises(ValueError):
            self.app_data.find_suitable_truck(3000, 300)

    def test_find_delivery_route(self):
        route1 = self.app_data.create_delivery_route("10:00", "12:00", Locations.MEL.value, Locations.SYD.value, Locations.BRI.value)
        route2 = self.app_data.create_delivery_route("12:00", "14:00", Locations.SYD.value, Locations.BRI.value, Locations.PER.value)
        self.assertEqual(self.app_data.find_delivery_route(route1.id), route1)
        self.assertEqual(self.app_data.find_delivery_route(route2.id), route2)
        with self.assertRaises(ValueError):
            self.app_data.find_delivery_route(999)

    def test_assign_truck_to_route(self):
        self.app_data._create_trucks()
        
        valid_truck_id = 1001 
        truck = next(truck for truck in self.app_data.trucks if truck.truck_id == valid_truck_id)
        
        route = self.app_data.create_delivery_route("10:00", "12:00", Locations.MEL.value, Locations.SYD.value, Locations.PER.value)
        
        self.app_data.assign_truck_to_route(route.id, truck.truck_id)
        
        self.assertEqual(route.truck, truck)
