from models.delivery_package import DeliveryPackage
from models.user import User
from models.employee_roles import EmployeeRoles
from models.employee import Employee
from Vehicles.truck_class_model import TruckConstants as tc
from Vehicles.truck_class_model import TruckModel
from models.locations import Locations
from models.delivery_route import DeliveryRoute


class AppData:
    
    def __init__(self) -> None:
        self._users: list[User] = list()
        self._employees: list[Employee] = list()
        self._logged_employee = []
        self._trucks: list[TruckModel] = list()
        self._delivery_routes: list[DeliveryRoute] = list()
        self._delivery_packages: list[DeliveryPackage] = list()
        

    def initialize_employees(self):
        self._employees.extend([
            Employee("Employee", "EmployeeLast", EmployeeRoles.EMPLOYEE, "employee_user", "password123!"),
            Employee("Supervisor", "SupervisorLast", EmployeeRoles.SUPERVISOR, "supervisor_user", "password456!"),
            Employee("Manager", "ManagerLast", EmployeeRoles.MANAGER, "manager_user", "password789!"),
            Employee("Admin", "AdminLast", EmployeeRoles.ADMIN, "admin_user", "password000!")
        ])

    @property        
    def users(self):
        return tuple(self._users)
    
    @property
    def logged_in_employee(self):
        if self.has_logged_in_employee:
            return self._logged_employee
        else:
            raise ValueError('There is no logged in employee.')

    @property
    def has_logged_in_employee(self):
        return self._logged_employee is not None

    def login(self, employee: Employee):
        if employee not in self._employees:
            raise ValueError('Employee is not recognized.')
        self._logged_employee = employee

    def logout(self):
        self._logged_employee = None

    @property
    def delivery_packages(self):
        return tuple(self._delivery_packages)
    
    @property
    def delivery_routes(self):
        return tuple(self._delivery_routes)
    
    @property
    def employees(self):
        return tuple(self._employees)
    
    @property
    def trucks(self):
        return tuple(self._trucks)
    

    def create_delivery_package(self, weight, starting_location, target_location, contact_info: User) -> DeliveryPackage:
        package = DeliveryPackage(weight, starting_location, target_location, contact_info)
        self._delivery_packages.append(package)
        return package
    
    def create_delivery_route(self, deprature_time, arrival_time, *destinations) -> DeliveryRoute:
        route_id = DeliveryRoute.generate_id()
        delivery_route = DeliveryRoute(route_id, deprature_time, arrival_time, destinations)
        self._delivery_routes.append(delivery_route)
        return delivery_route
    
    def find_delivery_route(self, start_point: Locations, end_point: Locations) -> DeliveryRoute:
        available_routes = []
        
        for route in self._delivery_routes:
            if start_point in route._destinations and end_point in route._destinations and route._destinations.index(end_point) > route._destinations.index(start_point):
                available_routes.append(route)
                
        return tuple(available_routes) if available_routes else f'No available routes for {start_point} - {end_point}'
        
    
    def find_package_by_id(self, package_id) -> DeliveryPackage:
        for package in self._delivery_packages:
            if package.id == package_id:
                return package
        raise ValueError(f'Package with ID {id} not found')
    
    def view_packages(self):
        packages = [str(package) for package in self._delivery_packages]
        
        return '\n'.join(packages)
    
    def view_employees(self):
        employees = [str(employee) for employee in self._employees]
        
        return '\n'.join(employees)
    
    def add_customer(self, firstname, lastname, phone_number, email) -> User:
        customer = User(firstname, lastname, phone_number, email)
        self._users.append(customer)
        return customer

    def find_customer_by_email(self, email) -> User:
        for user in self.users:
            if user.email == email:
                return user
        raise ValueError(f'User with e-mail {email} not found')
    
    def add_employee(self, firstname, lastname, role: EmployeeRoles) -> Employee:
        employee = Employee(firstname, lastname, role)
        self._employees.append(employee)
        return employee
    
    # TODO
    def assign_package_to_truck(self, package_id, truck_id):
        pass #assign truck and package Ico
    
    def assign_truck_to_route(self, id):
        pass #Ico
    
    def find_truck_by_weight(self, weight):
        pass #ico

    def find_truck_by_km(self, km):
        pass #ico

    
    def get_truck_by_id(self, truck_id: int) -> TruckModel:
        for truck in self.trucks:
            if truck.truck_id == truck_id:
                return truck
        raise ValueError(f'Truck ID {truck_id} does not exist.')

    def _create_trucks(self):
        for truck_id in range(tc.SCANIA_MIN_ID, tc.SCANIA_MAX_ID + 1):
            self.trucks.extend(TruckModel(truck_id, tc.SCANIA_CAPACITY, tc.SCANIA_MAX_RANGE, "Scania"))

        for truck_id in range(tc.MAN_MIN_ID, tc.MAN_MAX_ID + 1):
            self.trucks.extend(TruckModel(truck_id, tc.MAN_CAPACITY, tc.MAN_MAX_RANGE, "Man"))

        for truck_id in range(tc.ACTROS_MIN_ID, tc.ACTROS_MAX_ID + 1):
            self.trucks.extend(TruckModel(truck_id, tc.ACTROS_CAPACITY, tc.ACTROS_MAX_RANGE, "Actros"))
