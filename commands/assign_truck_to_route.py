from datetime import datetime
from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from commands.constants.constants import OPERATION_CANCELLED, CANCEL, COMPLETED
from colorama import Fore
from commands.interaction_loops.get_id import GetId

class AssignTruckToRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)
        

    def execute(self): 
        super().execute()
        get_id = GetId(self._app_data)
        
        route_id = get_id.loop(Fore.LIGHTCYAN_EX + ' Input route ID: ')
        if route_id == CANCEL:
            return OPERATION_CANCELLED
        
        route = self._app_data.get_route_by_id(route_id)
        # da se oprawi da se syzdawa now route ako sme abore truck capacity za tozi route

        if route._status == COMPLETED:
            raise ValueError(Fore.RED + "Cannot create delivery for a completed route.")        
        suitable_trucks = self._app_data.find_suitable_truck_by_distance(route.total_distance)
        
        if not suitable_trucks:
            raise ValueError(Fore.RED + "No suitable truck available for this route distance.")
        
        suitable_trucks_by_weight = self._app_data.find_suitable_trucks_by_weight(suitable_trucks, route)
        
        if not suitable_trucks_by_weight:
            raise ValueError(Fore.RED + "No suitable truck available for package(s) weight.")
        
        final_trucks = self._app_data.show_available_trucks(suitable_trucks_by_weight)
        print(final_trucks)
        selected_truck = get_id.loop(Fore.LIGHTCYAN_EX + ' Select truck ID to assign to route: ')
        
        truck = self._app_data.get_truck_by_id(selected_truck)
        result = self._app_data.assign_truck_to_route(truck, route)
        return Fore.GREEN + result if 'successfully' in result else Fore.RED + result

    def _requires_login(self) -> bool:
        return True