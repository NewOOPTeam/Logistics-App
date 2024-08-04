from models.delivery_package import DeliveryPackage
from models.user import User
from models.locations import Locations
from models.employee_roles import EmployeeRoles
from models.emplyee import Employee
class AppData:
    
    def __init__(self) -> None:
        self._users: list[User] = list()
        self._delivery_packages = list()
        self._employees = list()
    
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
    
    def add_customer(self, firstname, lastname, phone_number, email) -> User:
        customer = User(firstname, lastname, phone_number, email)
        self._users.append(customer)
        return customer

    def add_employee(self, firstname, lastname, role: EmployeeRoles) -> Employee:
        employee = Employee(firstname, lastname, role)
        self._employees.append(employee)
        return employee
    
    def find_customer_by_email(self, email) -> User:
        for user in self.users:
            if user.email == email:
                return user
            
        raise ValueError(f'User with e-mail {email} not found')


# app_data = AppData()
# app_data.add_customer('Alexander', 'Vankov', '0877003723', 'sgdjf@ajd.com')
# app_data.create_delivery_package(15, Locations.SYD, Locations.BRI, app_data.users[0])
# print(app_data.delivery_packages)
# print(app_data.users)