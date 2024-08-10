from models.delivery_package import DeliveryPackage
from models.user import User
from models.employee_roles import EmployeeRoles
from models.employee import Employee
from Vehicles.truck_class_model import TruckConstants as tc
from Vehicles.truck_class_model import TruckModel
from models.route_stop import RouteStop
from models.locations import Locations
from models.delivery_route import DeliveryRoute
from date_time.date_time_functionalities import DateTime
from csv_file.distance_calculator import DistanceCalculator as DC


class AppData:
    
    def __init__(self) -> None:
        self._users: list[User] = list()
        self._employees: list[Employee] = list()
        self._logged_employee = None
        self._trucks: list[TruckModel] = list()
        self._delivery_routes: list[DeliveryRoute] = list()
        self._delivery_packages: list[DeliveryPackage] = list()

        self.initialize_employees()  # Initialize employees pod vapros
        self._create_trucks()  # Initialize trucks pod vapros
        

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
        return self._logged_employee

    @logged_in_employee.setter
    def logged_in_employee(self, employee):
        self._logged_employee = employee

    @property
    def has_logged_in_employee(self):
        return self._logged_employee is not None

    def login(self, employee):
        if employee not in self._employees:
            raise ValueError('Employee is not recognized.')
        if self.logged_in_employee is not None:
            raise ValueError('There is already a user logged in.')
        self.logged_in_employee = employee

    def logout(self):
        if self.logged_in_employee is None:
            raise ValueError('No user is currently logged in.')
        self.logged_in_employee = None

    def find_employee_by_username(self, username: str): #dobaveno ot men
        for employee in self._employees:
            if employee.username == username:
                return employee
        raise ValueError('Employee not found!')

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
    
    def create_delivery_route(self, deprature_time, arrival_time, route_stops, total_distance) -> DeliveryRoute:
        route_id = DeliveryRoute.generate_id()
        delivery_route = DeliveryRoute(route_id, deprature_time, arrival_time, route_stops, total_distance)
        self._delivery_routes.append(delivery_route)
        return delivery_route
    
    
    def calculate_route_times(self, route): #could take departure_time as argument depending on user input????
        starting_location = route[0]
        departure_time = DateTime.create_time_stamp_for_today() 
        start_location = RouteStop(starting_location, departure_time, departure_time)
        
        locations = route[1:]
        route_stops = [start_location]

        distance_calculator = DC()

        previous_location = starting_location
        previous_time = departure_time
        
        for location in locations:
            pointA_pointB = [previous_location, location]
            distance = distance_calculator.calculate_total_distance(route=pointA_pointB)
            arrival_time = DateTime.get_arrival_time_str(previous_time, distance)
        
            route_stops.append(RouteStop(location, departure_time, arrival_time))
            
            print(f"Arrival at {location}: {arrival_time}")
            
            previous_location = location
            previous_time = arrival_time

        # route = list(route)
            
        # total_distance = distance_calculator.get_route_distance(route)
        delivery_route = self.create_delivery_route(departure_time, arrival_time, route_stops, total_distance = 1019)
        print('created')
        print(route_stops)
        return delivery_route

    
    
    def find_delivery_route(self, start_point: Locations, end_point: Locations) -> DeliveryRoute:
        if start_point not in Locations or end_point not in Locations:
            return f'Invalid start or end point: {start_point}, {end_point}' #Proverka dali start_point i end_point sa vuv validnite lokacii
       
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
        employees = [
            f"{employee.firstname} {employee.lastname}, Role: {employee.role}, Username: {employee.username}"
            for employee in self._employees
        ]
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
    
    def add_employee(self, firstname, lastname, role: EmployeeRoles, username: Employee, pw: Employee) -> Employee:
        employee = Employee(firstname, lastname, role, username, pw)
        self._employees.append(employee)
        return employee
   
    def get_truck_by_id(self, truck_id: int) -> TruckModel:
        for truck in self.trucks:
            if truck.truck_id == truck_id:
                return truck
        raise ValueError(f'Truck ID {truck_id} does not exist.')
    
    # def _create_trucks(self):
    #     for truck_id in range(tc.SCANIA_MIN_ID, tc.SCANIA_MAX_ID + 1):
    #         self.trucks.extend(TruckModel(truck_id, tc.SCANIA_CAPACITY, tc.SCANIA_MAX_RANGE, "Scania"))
 
    #     for truck_id in range(tc.MAN_MIN_ID, tc.MAN_MAX_ID + 1):
    #         self.trucks.extend(TruckModel(truck_id, tc.MAN_CAPACITY, tc.MAN_MAX_RANGE, "Man"))
 
    #     for truck_id in range(tc.ACTROS_MIN_ID, tc.ACTROS_MAX_ID + 1):
    #         self.trucks.extend(TruckModel(truck_id, tc.ACTROS_CAPACITY, tc.ACTROS_MAX_RANGE, "Actros"))
        
    def _create_trucks(self):
        # Create SCANIA trucks
        scania_trucks = [TruckModel(truck_id, tc.SCANIA_CAPACITY, tc.SCANIA_MAX_RANGE, "Scania")
        for truck_id in range(tc.SCANIA_MIN_ID, tc.SCANIA_MAX_ID + 1)]
        self._trucks.extend(scania_trucks)
 
        # Create MAN trucks
        man_trucks = [TruckModel(truck_id, tc.MAN_CAPACITY, tc.MAN_MAX_RANGE, "Man")
        for truck_id in range(tc.MAN_MIN_ID, tc.MAN_MAX_ID + 1)]
        self._trucks.extend(man_trucks)
 
        # Create ACTROS trucks
        actros_trucks = [TruckModel(truck_id, tc.ACTROS_CAPACITY, tc.ACTROS_MAX_RANGE, "Actros")
        for truck_id in range(tc.ACTROS_MIN_ID, tc.ACTROS_MAX_ID + 1)]
        self._trucks.extend(actros_trucks)
            
            
    def assign_package_to_delivery_route(self, package_id: int, route_id: int):
        package = self.find_package_by_id(package_id)
        route = self.get_route_by_id(route_id)
        route.assign_package(package)
 
    def find_suitable_truck(self, weight: DeliveryPackage, km: int):
        for truck in self._trucks:
            if weight <= truck._truck_capacity and km <= truck.max_range:
                return truck
        raise ValueError("No suitable truck found") #status sushto da se impl
 
    def get_route_by_id(self, id: int) -> DeliveryRoute:
        for route in self._delivery_routes:
            if route.id == id:
                return route
        raise ValueError(f'Route with ID {id} not found.')
    
    def assign_truck_to_route(self, route_id: int, truck_id: int):
        truck = self.get_truck_by_id(truck_id)
        route = self.get_route_by_id(route_id)
        route.assign_truck(truck) # da se proveri

    def find_unassigned_packages(self):
        unassigned_packages = [package for package in self._delivery_packages if package.status == DeliveryPackage.UNASSIGNED]
        return '\n\n'.join(unassigned_packages)
