from models.delivery_package import DeliveryPackage
from models.user import User


class AppData:
    
    def __init__(self) -> None:
        self._users: list[User] = list()
    
    @property        
    def users(self):
        return self._users
    
    def create_delivery_package(self, weight, starting_location, target_location, contact_info) -> DeliveryPackage:
        package = DeliveryPackage(weight, starting_location, target_location, contact_info)
        
        return package
    
    def add_customer(self, firstname, lastname, phone_number, email) -> User:
        customer = User(firstname, lastname, phone_number, email)
        self._users.append(customer)
        return customer
    
    def find_customer_by_email(self, email) -> User:
        for user in self.users:
            if user.email == email:
                return user
            
        raise ValueError(f'User with e-mail {email} not found')
        
        