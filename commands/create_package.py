from core.application_data import AppData
from commands.base_command import BaseCommand
from commands.helper_methods import Validate
from commands.interaction_loops.get_weight import GetWeight
from commands.interaction_loops.get_start_end_location import GetStartEndLocation
from commands.interaction_loops.find_customer_by_email import GetCustomerInfo
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from colorama import Fore

class CreatePackage(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)

    ### add start date!!!!!

    def execute(self):
        
        get_weight = GetWeight(self._app_data)
        weight = get_weight.loop(Fore.LIGHTCYAN_EX + ' Input package weight: ')
        
        if weight == CANCEL:
            return OPERATION_CANCELLED
        
        get_start_end_location = GetStartEndLocation(self._app_data)
        route = get_start_end_location.loop(Fore.LIGHTCYAN_EX + ' Input start and end destination: ')
      
        if route == CANCEL:
            return OPERATION_CANCELLED
      
        get_customer_info = GetCustomerInfo(self._app_data)
        customer = get_customer_info.loop(Fore.LIGHTCYAN_EX + ' Input customer email address: ')

        if customer == CANCEL:
            return OPERATION_CANCELLED
        
        package = self._app_data.create_delivery_package(weight, route, customer)
        
        return Fore.GREEN + f'Package with ID #{package.id} was created'
    
