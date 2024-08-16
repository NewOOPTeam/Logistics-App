from datetime import datetime
from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from commands.constants.constants import OPERATION_CANCELLED, CANCEL
from colorama import Fore
from commands.interaction_loops.get_id import GetId

class AssignTruckToRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 1, self.__class__.__name__)
        # self.truck_id = int(params[0])
        # self.route_id = int(params[1])
        super().__init__(params, app_data)
        

    def execute(self): 
        super().execute()
        get_id = GetId(self._app_data)
        
        # truck = self._app_data.get_truck_by_id(self.truck_id)
        self.route_id = int(self.params[0])
        route = self._app_data.get_route_by_id(self.route_id)
        suitable_trucks = self._app_data.find_suitable_truck(route.total_distance)
        combined_weight = route.calculate_weight_at_start()
       
        if not suitable_trucks:
            raise ValueError(Fore.RED + "No suitable truck available.")
        suitable_trucks_by_weight = self._app_data.find_suitable_truck_by_weight(suitable_trucks, combined_weight)
        
        if not suitable_trucks_by_weight:
            raise ValueError(Fore.RED + "No suitable truck available. BY WEIGHT")
        
        suitable_trucks_by_weight_str = [str(truck) for truck in suitable_trucks_by_weight]
        print("\n".join(suitable_trucks_by_weight_str))
        selected_truck = get_id.loop(Fore.LIGHTCYAN_EX + ' Input truck ID: ')
        truck = self._app_data.get_truck_by_id(selected_truck)


        # if truck:
        #     package = self._app_data.assign_package_to_truck(truck, package.id)
        #     return f'Delivery created for Package #{package.id}, expected arrival: ' + f'\nPackage info:\n{package}\n' + f'{truck.truck_capacity}' # tuk moje bi da ima arrival time? i mai za da stane, tr w delivery    packages wmesto locations da ima route_stops
        
        # if not truck:
        #     return Fore.RED + f'Truck with ID {self.truck_id} does not exist.'
        
        # if not route:
        #     return Fore.RED + f'Route with ID {self.route_id} does not exist.'
        
        result = self._app_data.assign_truck_to_route(truck, route)
        return Fore.GREEN + result if 'successfully' in result else Fore.RED + result

    def _requires_login(self) -> bool:
        return True
