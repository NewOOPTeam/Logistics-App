from models.delivery_package import DeliveryPackage
from models.user import User
from models.employee_roles import EmployeeRoles
from models.employee import Employee


class AppData:
    
    def __init__(self) -> None:
        self._users: list[User] = list()
        self._employees: list[Employee] = list()
        
        # self._delivery_routes = list()
        self._delivery_packages: list[DeliveryPackage] = list()

        
    @property        
    def users(self):
        return self._users

    @property
    def delivery_packages(self):
        return self._delivery_packages

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
    
    def assign_package_to_delivery_route(self, id):
        pass