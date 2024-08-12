from models.delivery_package import ASSIGNED, DeliveryPackage
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
from colorama import Fore


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
        

    @property        
    def users(self):
        return tuple(self._users)
    
    @property
    def employees(self):
        return tuple(self._employees)
    
    @property
    def trucks(self):
        return tuple(self._trucks)
    
    @property
    def has_logged_in_employee(self):
        return self._logged_employee is not None
    
    @property
    def delivery_packages(self):
        return tuple(self._delivery_packages)
    
    @property
    def delivery_routes(self):
        return tuple(self._delivery_routes)
    
    @property
    def logged_in_employee(self):
        return self._logged_employee

    @logged_in_employee.setter
    def logged_in_employee(self, employee):
        self._logged_employee = employee


    def initialize_employees(self):
        self._employees.extend([
            Employee("Employee", "EmployeeLast", EmployeeRoles.EMPLOYEE, "employee_user", "password123!"),
            Employee("Supervisor", "SupervisorLast", EmployeeRoles.SUPERVISOR, "supervisor_user", "password456!"),
            Employee("Manager", "ManagerLast", EmployeeRoles.MANAGER, "manager_user", "password789!"),
            Employee("Admin", "AdminLast", EmployeeRoles.ADMIN, "admin_user", "password000!")
        ])

    def add_employee(self, firstname, lastname, role: EmployeeRoles, username: Employee, pw: Employee) -> Employee:
        employee = Employee(firstname, lastname, role, username, pw)
        self._employees.append(employee)
        return employee

    def find_employee_by_username(self, username: str):
        for employee in self._employees:
            if employee.username == username:
                return employee
        raise ValueError(Fore.RED + 'Employee not found!')
   
    def view_employees(self):
        employees = [Fore.LIGHTCYAN_EX +
            f"{employee.firstname} {employee.lastname}, Role: {employee.role}, Username: {employee.username}"
            for employee in self._employees
        ]
        return '\n'.join(employees)
   
    def login(self, employee):
        if employee not in self._employees:
            raise ValueError(Fore.RED + 'Employee is not recognized.')
        if self.logged_in_employee is not None:
            raise ValueError(Fore.RED + 'There is already a user logged in.')
        self.logged_in_employee = employee

    def logout(self):
        if self.logged_in_employee is None:
            raise ValueError(Fore.RED + 'No user is currently logged in.')
        self.logged_in_employee = None
        
    def user_exists(self, username) -> bool:
        for employee in self._employees:
            if username == employee.username:
                return True
        return False
            

    def add_customer(self, firstname, lastname, phone_number, email) -> User:
        customer = User(firstname, lastname, phone_number, email)
        self._users.append(customer)
        return customer

    def find_customer_by_email(self, email) -> User:
        for user in self.users:
            if user.email == email:
                return user
        raise ValueError(Fore.RED + f'User with e-mail {email} not found')
    
    def customer_exists(self, email) -> bool:
        for user in self.users:
            if user.email == email:
                return True
        return False

    def create_delivery_package(self, weight, route, contact_info: User) -> DeliveryPackage:
        starting_location, target_location = route
        package = DeliveryPackage(weight, starting_location, target_location, contact_info)
        self._delivery_packages.append(package)
        return package
     
    def find_package_by_id(self, package_id) -> DeliveryPackage:
        for package in self._delivery_packages:
            if package.id == package_id:
                return package
        raise ValueError(Fore.RED + f'Package with ID {package_id} not found')
    
    def view_packages(self):
        packages = [str(package) for package in self._delivery_packages]
        output = '\n'.join(packages)
        if not packages:
            output = Fore.YELLOW + 'No packages to show'
        return output
    
    def get_package_locations(self, package_id: int):
        package = self.find_package_by_id(package_id)
        return package.start_location, package.end_location

    def create_delivery_route(self, deprature_time, arrival_time, route_stops: list[RouteStop]) -> DeliveryRoute:
        dc = DC()
        locations = [loc.location for loc in route_stops]
        total_distance = dc.calculate_total_distance(locations)
        
        route_id = DeliveryRoute.generate_id()
        delivery_route = DeliveryRoute(route_id, deprature_time, arrival_time, route_stops, total_distance)
        self._delivery_routes.append(delivery_route)
        return delivery_route
    
    
    def get_route_by_id(self, id: int) -> DeliveryRoute:
        for route in self._delivery_routes:
            if route.id == id:
                return route
        raise ValueError(Fore.RED + f'Route with ID {id} not found.')
    
    def view_all_delivery_routes(self):
        routes = [str(route) for route in self._delivery_routes]
        return '\n'.join(routes)
    
    def calculate_route_times(self, route): #could take departure_time as argument depending on user input????
        starting_location = route[0] #ADL
        # departure_time = DateTime.create_time_stamp_for_today() 
        departure_time = 'Oct 10 2024 06:00h'
        start_location = RouteStop(starting_location, departure_time, departure_time)
        
        locations = route[1:]
        route_stops = [start_location]

        distance_calculator = DC()

        previous_location = starting_location
        previous_time = departure_time
        
        for location in locations:
            pointA_pointB = [previous_location, location]
            distance = distance_calculator.calculate_total_distance(pointA_pointB)
            arrival_time = DateTime.get_arrival_time_str(previous_time, distance)
        
            previous_location = location
            previous_time = arrival_time
            route_stops.append(RouteStop(location, previous_time, arrival_time))
            # print(f"Arrival at {location}: {arrival_time}")

        # route = list(route)
            
        # total_distance = distance_calculator.get_route_distance(route)
        delivery_route = self.create_delivery_route(departure_time, arrival_time, route_stops)

        return delivery_route
    

    # def find_valid_routes_for_package(self, package_id: int):
        
        # start_location, end_location = self.get_package_locations(package_id)
        
        # valid_routes = []
        
        # for route in self._delivery_routes:
        #     destinations = [stop.location for stop in route.destinations]
        #     if start_location in route.destinations and end_location in route.destinations:
        #         start_index = route.destinations.index(start_location)
        #         end_index = route.destinations.index(end_location)
        #         if start_index < end_index:
        #             valid_routes.append(route)
        
        # return valid_routes
    
    def find_valid_routes_for_package(self, package_id: int):
        start_location, end_location = self.get_package_locations(package_id)
        
        # Convert start_location and end_location to Locations enum if not already
        if not isinstance(start_location, Locations):
            start_location = Locations[start_location]
        if not isinstance(end_location, Locations):
            end_location = Locations[end_location]
        
        valid_routes = []
        
        for route in self._delivery_routes:
            destinations = [stop.location for stop in route.destinations]
            if start_location in destinations and end_location in destinations:
                start_index = destinations.index(start_location)
                end_index = destinations.index(end_location)
                if start_index < end_index:
                    valid_routes.append(route)
        
        return valid_routes
    
    def list_valid_routes(self, package_id: int):
        valid_routes = self.find_valid_routes_for_package(package_id)
        
        if not valid_routes:
            return Fore.RED + f'No valid routes available for package ID {package_id}.'
    
        route_ids = [route.id for route in valid_routes]
        
        return route_ids

    def assign_package_to_route(self, package_id: int, route_id: int):
        package = self.find_package_by_id(package_id)
                
        valid_routes = self.find_valid_routes_for_package(package_id)
        
        route = next((r for r in valid_routes if r.id == route_id), None)
        
        if route is None:
            raise ValueError(Fore.RED + f'Route ID {route_id} is not a valid route for package ID {package_id}.')
        
        if package.status == ASSIGNED:
            raise ValueError(Fore.RED + f'Package ID {package_id} is already assigned to a route.')
        
        package.status = ASSIGNED
        package._assigned_route = route

        return package
    
    def find_unassigned_packages(self):
        unassigned_packages = [package for package in self._delivery_packages if package.status == DeliveryPackage.UNASSIGNED]
        return '\n\n'.join(unassigned_packages)

    def _create_trucks(self):
        scania_trucks = [TruckModel(truck_id, tc.SCANIA_CAPACITY, tc.SCANIA_MAX_RANGE, "Scania")
        for truck_id in range(tc.SCANIA_MIN_ID, tc.SCANIA_MAX_ID + 1)]
        self._trucks.extend(scania_trucks)
 
        man_trucks = [TruckModel(truck_id, tc.MAN_CAPACITY, tc.MAN_MAX_RANGE, "Man")
        for truck_id in range(tc.MAN_MIN_ID, tc.MAN_MAX_ID + 1)]
        self._trucks.extend(man_trucks)

        actros_trucks = [TruckModel(truck_id, tc.ACTROS_CAPACITY, tc.ACTROS_MAX_RANGE, "Actros")
        for truck_id in range(tc.ACTROS_MIN_ID, tc.ACTROS_MAX_ID + 1)]
        self._trucks.extend(actros_trucks)

    def mark_unavailable(self, truck_id: int):
        truck = self.get_truck_by_id(truck_id)
        truck.status = 'Unavailable'

    def mark_available(self, truck_id: int):
        truck = self.get_truck_by_id(truck_id)
        truck.status = 'Available'

    def get_truck_by_id(self, truck_id: int) -> TruckModel:
        for truck in self.trucks:
            if truck.truck_id == truck_id:
                return truck
        raise ValueError(Fore.RED + f'Truck ID {truck_id} does not exist.')
 
    def find_suitable_truck(self, weight: DeliveryPackage, km: int):
        for truck in self._trucks:
            if weight <= truck._truck_capacity and km <= truck.max_range:
                return truck
        raise ValueError(Fore.RED + "No suitable truck found")
    
                
    # def assign_package_to_delivery_route(self, package_id: int, route_id: int): #- Shte go ostavq tuk za momenta.
    #     if route_id >= len(self._delivery_routes) or route_id < 0:
    #         raise ValueError('Invalid route ID')

    #     route = self._delivery_routes[route_id]
        
    #     package = self.find_package_by_id(package_id)
        
    #     if package._start_location not in route._destinations or package._end_location not in route._destinations:
    #         raise ValueError('Package start or end location is not in the route destinations')
        
    #     start_index = route._destinations.index(package._start_location)
    #     end_index = route._destinations.index(package._end_location)
        
    #     if start_index >= end_index:
    #         raise ValueError('Start location must be before end location in the route')

    #     package.status = ASSIGNED
    #     package._assigned_route = route
    #     return package
