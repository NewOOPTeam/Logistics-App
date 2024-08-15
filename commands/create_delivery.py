from core.application_data import AppData
from commands.base_command import BaseCommand
from commands.helper_methods import Validate
from commands.interaction_loops.get_id import GetId
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from colorama import Fore


class CreateDelivery(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)

    def execute(self):
        super().execute()
        
        get_id = GetId(self._app_data)
        id = get_id.loop(Fore.LIGHTCYAN_EX + ' Input package ID: ')
        if id == CANCEL:
            return OPERATION_CANCELLED
        
        valid_routes = self._app_data.find_valid_routes_for_package(id) 
        if not valid_routes:
            return Fore.RED + 'No valid routes available for package ID.'
        # # 10500km - ACtros
        # distances = [r.total_distance for r in valid_routes]
        # suitable_truck = []
        # for distance in distances:
        #     suitable_truck.extend(self.app_data.find_suitable_truck(distance))
        # if not suitable_truck:
        #     raise ValueError(Fore.RED + 'No suitable trucks available.') 
        




        
        ## assign truck automatically
        ## assignpackage to truck method
        ## automatically  when the date/time is correct
        
        return valid_routes
    
    def _requires_login(self) -> bool:
        return True