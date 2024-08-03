from core.application_data import AppData
from commands.base_command import BaseCommand
from commands.helper_methods import Parse

class CreatePackage(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        super().__init__(params, app_data)

        
    # Creating a delivery package – unique id, start location, end location and weight in kg, and contact information for the customer.


    def execute(self):
        weight, starting_location, target_location, contact_info = self._params
        weight = Parse.to_float(weight)
        contact = self._app_data.find_customer(contact_info)
        package = self._app_data.create_delivery_package(weight, starting_location, target_location, contact)
        
        return f'Package with ID {package.id} was created'
    
