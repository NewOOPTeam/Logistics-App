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
        ################### UNFINISHED #####################

        # Creating a delivery route – should have a unique id, and a list of locations (at least two).
        # datetime
        # expected delivery date
        # route needs to be assigned an ID, so we need to create a DeliveryRoute class
        
        # The first location is the starting location – it has a departure time.
        # The other locations have expected arrival time.

        # package = FindPackage(self._app_data).loop(' Input package ID: ') - da premahnem package- da ostavim samo route
        # if package == OPERATION_CANCELLED:
        #     return OPERATION_CANCELLED

        route = CreateRoute(self._app_data).loop(Fore.LIGHTCYAN_EX + ' Input delivery route stops: ')
        if route == CANCEL:
            return OPERATION_CANCELLED
        
        delivery_route = self._app_data.calculate_route_times(route)
        
        return Fore.GREEN + f'Delivery route created: \n{str(delivery_route)}'


        # def get_arrival_time:
            # choice 1 - asap
            # choice 2 - input
        
        # package ID
        # route
        




            
 
    def get_start_date(self):
        pass

