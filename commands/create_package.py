from core.application_data import AppData
from commands.base_command import BaseCommand
from commands.helper_methods import Validate
from commands.interaction_loops.get_weight import GetWeight
from commands.interaction_loops.get_start_end_location import GetStartEndLocation
from commands.interaction_loops.find_customer_by_email import GetCustomerInfo
from commands.interaction_loops.get_id import GetId
from commands.interaction_loops.create_route import CreateRoute
from commands.interaction_loops.validate_route import ValidateRoute
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from colorama import Fore

class CreatePackage(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)

    ### add start date!!!!!

    def execute(self):
        get_weight = GetWeight(self._app_data)
        get_start_end_location = GetStartEndLocation(self._app_data)
        get_customer_info = GetCustomerInfo(self._app_data)
        get_id = GetId(self._app_data)
        get_route = CreateRoute(self._app_data)
        validated_route = ValidateRoute(self._app_data)

        
        
        weight = get_weight.loop(Fore.LIGHTCYAN_EX + ' Input package weight: ')
        if weight == CANCEL:
            return OPERATION_CANCELLED
        
        route = get_start_end_location.loop(Fore.LIGHTCYAN_EX + ' Input start and end destination: ')
        if route == CANCEL:
            return OPERATION_CANCELLED
      
        customer = get_customer_info.loop(Fore.LIGHTCYAN_EX + ' Input customer email address: ')
        if customer == CANCEL:
            return OPERATION_CANCELLED
        
        package = self._app_data.create_delivery_package(weight, route, customer)
        print(Fore.GREEN + f'Package with ID #{package.id} was created')
        
        valid_routes = self._app_data.find_valid_routes_for_package(package.id)
        
        if not valid_routes:
            new_route = get_route.loop(Fore.LIGHTCYAN_EX + ' No available delivery routes at the time, please create a new one!\n Input delivery route stops: ')
            validated_route = validated_route.loop(route, new_route)
            if validated_route == CANCEL:
                return OPERATION_CANCELLED
        else:
            self.display_delivery_routes(valid_routes)
            route_id = get_id.loop(Fore.LIGHTCYAN_EX + ' Select route (input route ID): ')
            if route_id == CANCEL:
                return OPERATION_CANCELLED
            
        return 'evala'
        
        
        
        
        
        
        
    def display_delivery_routes(self, valid_routes):
        output = []
        for route in valid_routes:
            output.append(str(route))
        
        return 'Suitable delivery routes for this package: ' + '\n'.join
        
    def _requires_login(self) -> bool:
        return True
