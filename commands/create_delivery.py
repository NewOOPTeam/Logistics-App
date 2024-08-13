from core.application_data import AppData
from commands.base_command import BaseCommand
from commands.helper_methods import Validate
from commands.interaction_loops.get_id import GetId
from commands.interaction_loops.get_start_end_location import GetStartEndLocation
from commands.interaction_loops.find_customer_by_email import GetCustomerInfo
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from colorama import Fore

class CreateDelivery(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)

    def execute(self):
        get_id = GetId(self._app_data)
        id = get_id.loop(Fore.LIGHTCYAN_EX + ' Input package ID: ')
        if id == CANCEL:
            return OPERATION_CANCELLED
        
        valid_routes = self._app_data.list_valid_routes(id) 
        
        ## assign truck automatically
        ## assignpackage to truck method
        ## automatically  when the date/time is correct
        
        return valid_routes
    
    def _requires_login(self) -> bool:
        return False