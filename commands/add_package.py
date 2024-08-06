from core.application_data import AppData
from commands.base_command import BaseCommand
from commands.helper_methods import Parse, Validate
from models.locations import Locations

class AddPackage(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 4, self.__class__.__name__)
        super().__init__(params, app_data)

        
    # Creating a delivery package – unique id, start location, end location and weight in kg, and contact information for the customer.

    ### add start date!!!!!

    def execute(self):
        weight, starting_location, target_location, contact_info = self._params
        
        weight = Parse.to_float(weight)
        starting_location = Locations.from_string(starting_location)
        target_location = Locations.from_string(target_location)
        
        contact = self._app_data.find_customer_by_email(contact_info)
        
        package = self._app_data.create_delivery_package(weight, starting_location, target_location, contact)
        
        return f'Package with ID #{package.id} was created'
    
