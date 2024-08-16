from models.delivery_package import ASSIGNED_TO_ROUTE, ASSIGNED_TO_TRUCK, DeliveryPackage
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
    def users(self) -> tuple:
        return tuple(self._users)
    
    @property
    def employees(self) -> tuple:
        return tuple(self._employees)
    
    @property
    def trucks(self) -> tuple:
        return tuple(self._trucks)
    
    @property
    def has_logged_in_employee(self) -> bool:
        return self._logged_employee is not None
    
    @property
    def delivery_packages(self) -> tuple:
        return tuple(self._delivery_packages)
    
    @property
    def delivery_routes(self) -> tuple:
        return tuple(self._delivery_routes)
    
    @property
    def logged_in_employee(self) -> Employee:
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

    def add_employee(self, firstname, lastname, role: EmployeeRoles, username, password: Employee) -> Employee:
        """creates an instance of the Employee class and adds it to the list of employees

        Args:
            firstname (str): should be at least 3 characters long and no whitespace
            lastname (str): should be at least 3 characters long and no whitespace
            role (EmployeeRoles): employee role
            username (str): should be between 3 and 20 characters long, should contain only letters, digits, and special symbols "!@#$_" and no whitespace
            password (str): should be between 3 and 20 characters long and should contain only letters, digits, and special symbols "!@#$"

        Returns:
            (Employee)
        """
        employee = Employee(firstname, lastname, role, username, password)
        self._employees.append(employee)
        return employee

    def find_employee_by_username(self, username: str) -> Employee:
        """searches for an existing employee by username

        Args:
            username (str)

        Returns:
            (Employee)
        """
        for employee in self._employees:
            if employee.username == username:
                return employee
        raise ValueError(Fore.RED + 'Employee not found!')
   
    def view_employees(self) -> str:
        """shows all employees

        Returns:
            (str)
        """
        employees = [Fore.LIGHTCYAN_EX +
            f"{employee.firstname} {employee.lastname}, Role: {employee.role}, Username: {employee.username}"
            for employee in self._employees
        ]
        return '\n'.join(employees)
   
    def login(self, employee) -> None:
        """sets the current logged user to the user that is given as argument

        Args:
            employee (Employee)
        """
        if employee not in self._employees:
            raise ValueError(Fore.RED + 'Employee is not recognized.')
        if self.logged_in_employee is not None:
            raise ValueError(Fore.RED + 'There is already a user logged in.')
        self.logged_in_employee = employee

    def logout(self) -> None:
        """sets the current logged user to None
        """
        if self.logged_in_employee is None:
            raise ValueError(Fore.RED + 'No user is currently logged in.')
        self.logged_in_employee = None
        
    def user_exists(self, username) -> bool:
        """checks if a user with the given username exists in the list of employees.

        Args:
            username (str)

        Returns:
            (bool)
        """
        for employee in self._employees:
            if username == employee.username:
                return True
        return False
            

    def add_customer(self, firstname, lastname, phone_number, email) -> User:
        """creates an instance of the User class and adds it to the list of existing customers

        Args:
            firstname (str): should be at least 3 characters long and no whitespace
            lastname (str): should be at least 3 characters long and no whitespace
            phone_number (str): should contain between 8 and 13 numeric characters, with the exception of the phone number being given starting with a "+" sign
            email (str): should be between 7 and 20 characters and must contain "@"

        Returns:
            (User)
        """
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
    
    def view_packages(self) -> str:
        """shows information about all packages that currently exist

        Returns:
            (str)
        """
        packages = [str(package) for package in self._delivery_packages]
        output = '\n\n'.join(packages)
        if not packages:
            output = Fore.YELLOW + 'No packages to show'
        return output
    
    def get_package_locations(self, package_id: int) -> tuple[Locations, Locations]:
        """finds the starting and final location of the given package

        Args:
            package_id (int)

        Returns:
            tuple(Locations, Locations):
        """
        package = self.find_package_by_id(package_id)
        return package.start_location, package.end_location

    def create_delivery_route(self, route) -> DeliveryRoute:
        dc = DC()
        route_stops = self.calculate_route_times(route)
        locations = [loc.location.name for loc in route_stops]
        
        route_id = DeliveryRoute.generate_id()
        total_distance = dc.calculate_total_distance(locations)
        delivery_route = DeliveryRoute(route_id, route_stops, total_distance)
        self._delivery_routes.append(delivery_route)
        return delivery_route
    
    
    def get_route_by_id(self, id: int) -> DeliveryRoute:
        for route in self._delivery_routes:
            if route.id == id:
                return route
        raise ValueError(Fore.RED + f'Route with ID {id} not found.')
    
    def get_packages_for_route(self, route_id: int) -> tuple:
        """shows all packages currently assigned to the given route

        Args:
            route_id (int)

        Returns:
            (tuple)
        """
        route = self.get_route_by_id(route_id)
        return route.packages

    # i want this method to retrun the route + the packages assigned to it
    def view_all_delivery_routes(self) -> str:# promqna 16;55
        routes_with_packages = []
        for route in self._delivery_routes:
            packages = self.get_packages_for_route(route.id)
            sum_of_weights = sum([package.weight for package in packages])
            route_info = f"Route: {route}\nAssigned packages: {len(packages)}, total weight: {sum_of_weights}\n" 
            routes_with_packages.append(route_info)
        return '\n\n'.join(routes_with_packages)

        # routes = [str(route) for route in self._delivery_routes]
        # return '\n'.join(routes)
    
    def calculate_route_times(self, route) -> list[RouteStop]:
        """calculates arrival and departure time at each stop for the delivery route

        Args:
            route (tuple): tuple containing each stop given as Locations.name

        Returns:
            list[RouteStop]: list containing information about each stop along the delivery route - location, arrival time and departure time
        """
        starting_location = route[0]
        departure_time = DateTime.create_time_stamp_for_today() 
        _starting_location = Locations[starting_location]
        start_location = RouteStop(_starting_location, departure_time, departure_time)
        
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
            _location = Locations[location]
            route_stops.append(RouteStop(_location, previous_time, arrival_time))

        return route_stops
    
    
    def find_valid_routes_for_package(self, package_id: int) -> list[DeliveryRoute]:
        """finds all delivery routes that contain the starting and final location of the given package

        Args:
            package_id (int)

        Returns:
            list[DeliveryRoute]
        """
        start_location, end_location = self.get_package_locations(package_id)
        
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
    
    # def list_valid_routes(self, package_id: int):
    #     valid_routes = self.find_valid_routes_for_package(package_id)
        
    #     if not valid_routes:
    #         return Fore.RED + f'No valid routes available for package ID {package_id}.'
    
    #     route_ids = [route.id for route in valid_routes]
        
    #     return route_ids


    def assign_package_to_route(self, package_id: int, route_id: int) -> DeliveryPackage:
        """assigns given package to the given route

        Args:
            package_id (int)
            route_id (int)

        Returns:
            (DeliveryPackage)
        """
        package = self.find_package_by_id(package_id)
        route = self.get_route_by_id(route_id)
                
        # valid_routes = self.find_valid_routes_for_package(package_id)
        
        # route = next((r for r in valid_routes if r.id == route_id), None)
        
        if route is None:
            raise ValueError(Fore.RED + f'Route ID {route_id} is not a valid route for package ID {package_id}.')
        
        if package.status == ASSIGNED_TO_ROUTE:
            raise ValueError(Fore.RED + f'Package ID {package_id} is already assigned to a route.')
        
        package.status = ASSIGNED_TO_ROUTE
        route._packages.append(package)
        package._assigned_route = route

        return package
    
    def find_unassigned_packages(self) -> str:
        """returns information about all packages with status UNASSIGNED

        Returns:
            (str)
        """
        unassigned_packages = [package for package in self._delivery_packages if package.status == DeliveryPackage.UNASSIGNED]
        return '\n\n'.join(unassigned_packages)

    def _create_trucks(self) -> None:
        """initializes all trucks at the start of the program
        """
        scania_trucks = [TruckModel(truck_id, tc.SCANIA_CAPACITY, tc.SCANIA_MAX_RANGE, "Scania")
        for truck_id in range(tc.SCANIA_MIN_ID, tc.SCANIA_MAX_ID + 1)]
        self._trucks.extend(scania_trucks)
 
        man_trucks = [TruckModel(truck_id, tc.MAN_CAPACITY, tc.MAN_MAX_RANGE, "Man")
        for truck_id in range(tc.MAN_MIN_ID, tc.MAN_MAX_ID + 1)]
        self._trucks.extend(man_trucks)

        actros_trucks = [TruckModel(truck_id, tc.ACTROS_CAPACITY, tc.ACTROS_MAX_RANGE, "Actros")
        for truck_id in range(tc.ACTROS_MIN_ID, tc.ACTROS_MAX_ID + 1)]
        self._trucks.extend(actros_trucks)

    def mark_unavailable(self, truck_id: int) -> None:
        """marks a truck unavailable

        Args:
            truck_id (int)
        """
        truck = self.get_truck_by_id(truck_id)
        truck.status = 'Unavailable'

    def mark_available(self, truck_id: int):
        """marks a truck available

        Args:
            truck_id (int)
        """
        truck = self.get_truck_by_id(truck_id)
        truck.status = 'Available'

    def find_suitable_truck(self, km: int) -> list[TruckModel]:
        """finds all available trucks with a suitable range for the given route distance

        Args:
            km (int): total distance of the delivery route

        Returns:
            list[TruckModel]
        """
        suitable_trucks = []
        for truck in self.trucks:  
            if truck.status == 'Available' and truck.truck_capacity >= km:
                suitable_trucks.append(truck)
        
        return suitable_trucks           
    
    def find_suitable_truck_by_weight(self, suitable_trucks, weight: int) -> TruckModel:
        """iterates through a list of trucks suitable for the total distance of the route
        and returns the first with a mathing capacity for the total weight
        of the assigned packages

        Args:
            suitable_trucks (list)
            weight (int)

        Returns:
            (TruckModel)
        """
        for truck in suitable_trucks:
            if truck.truck_capacity >= weight:
                return truck
    
    def assign_package_to_truck(self, truck, package_id: int) -> DeliveryPackage:
        """assignes the given package to the given truck

        Args:
            truck (TruckModel)
            package_id (int)

        Returns:
            (DeliveryPackage)
        """
        package = self.find_package_by_id(package_id)
        truck._packages.append(package)
        package.status = ASSIGNED_TO_TRUCK
        truck.truck_capacity -= package.weight
        return package

    def get_truck_by_id(self, truck_id: int) -> TruckModel:
        for truck in self.trucks:
            if truck.truck_id == truck_id:
                return truck
        raise ValueError(Fore.RED + f'Truck ID {truck_id} does not exist.')
 
    # def view_packages_of_route(self, route_id):
    #     route = self.find_route_by_id(route_id)
    #     print('\n'.join(route.packages))
    #     print(len(route.packages))
    #     weights = [package.weight for package in route.packages]
    #     print('Weights:\n')
    #     print('\n'.join(weights))
        
