from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from commands.interaction_loops.create_route import CreateRoute
from commands.constants.constants import OPERATION_CANCELLED, CANCEL
from colorama import Fore


class CreateDeliveryRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)
        
    def execute(self): 
        super().execute()
        
        route = CreateRoute(self._app_data).loop(Fore.LIGHTCYAN_EX + ' Input delivery route stops: ')
        if route == CANCEL:
            return OPERATION_CANCELLED

        departure_time = input(Fore.LIGHTCYAN_EX + ' Input departure time: ')
        delivery_route = self._app_data.create_delivery_route(route, departure_time)
        return Fore.GREEN + f'Delivery route created: \n{str(delivery_route)}'          
 
    def _requires_login(self) -> bool:
        return True
