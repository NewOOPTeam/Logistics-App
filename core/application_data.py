from models.delivery_package import DeliveryPackage
from models.user import User
from models.employee_roles import EmployeeRoles
from models.employee import Employee
from Vehicles.truck_class_model import TruckConstants as tc
from Vehicles.truck_class_model import TruckModel
from models.delivery_route import DeliveryRoute


class AppData:
    
    def __init__(self) -> None:
        self._users: list[User] = list()
        self._employees: list[Employee] = list()
        self._trucks: list[TruckModel] = list()
        self._delivery_routes: list[DeliveryRoute] = list()
        self._delivery_packages: list[DeliveryPackage] = list()

        
    @property        
    def users(self):
        return tuple(self._users)

    @property
    def delivery_packages(self):
        return tuple(self._delivery_packages)
    
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
    
    def find_package_by_id(self, id) -> DeliveryPackage:
        for package in self._delivery_packages:
            if package.id == id:
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
    def assign_package_to_delivery_route(self, package_id, truck_id):
        pass #assign truck and package
    
    def assign_truck_to_route(self, id):
        pass
    
    def find_truck_by_weight(self, weight):
        pass
    
    def select_shortest_route(self):
        pass
    
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
