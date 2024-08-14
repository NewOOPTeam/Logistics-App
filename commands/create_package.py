from core.application_data import AppData
from commands.base_command import BaseCommand
from commands.helper_methods import Validate
from commands.interaction_loops.get_weight import GetWeight
from commands.interaction_loops.get_start_end_location import GetStartEndLocation
from commands.interaction_loops.find_customer_by_email import GetCustomerInfo
from commands.interaction_loops.get_id import GetId
from commands.interaction_loops.create_route import CreateRoute
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from colorama import Fore


class CreatePackage(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)

    ### add start date!!!!!

    def execute(self):
        weight, route, customer, package = self.create_package()
        if any(weight, route, customer) == CANCEL:
            ### need to remove package from the lists and this is for other similar operations!!
            return OPERATION_CANCELLED
        
        valid_routes = self._app_data.find_valid_routes_for_package(package.id)
        if valid_routes:
            print(self.display_delivery_routes(valid_routes))
            route_id = self.select_route(valid_routes)
            new_route = self._app_data.get_route_by_id(route_id)
        else:
            new_route = self.create_route(route)
            if new_route == CANCEL:
                return OPERATION_CANCELLED
            
        suitable_trucks = self._app_data.find_suitable_truck(new_route.total_distance)
        
        if suitable_trucks:
            truck = self._app_data.find_suitable_truck_by_weight(suitable_trucks, package.weight)
            
        if truck:
            package = self._app_data.assign_package_to_truck(truck, package.id)
            return f'Delivery created for Package #{package.id}, expected arrival: ' + f'\nPackage info:\n{package}\n' # tuk moje bi da ima arrival time? i mai za da stane, tr w delivery    packages wmesto locations da ima route_stops
        return f'Delivery created for Package #{package.id}, awaiting assignment.'

        
    def _requires_login(self) -> bool:
        return True
        
    def create_package(self):
        get_weight = GetWeight(self._app_data)
        get_start_end_location = GetStartEndLocation(self._app_data)
        get_customer_info = GetCustomerInfo(self._app_data)

        weight = get_weight.loop(Fore.LIGHTCYAN_EX + ' Input package weight: ')
        if weight == CANCEL:
            return CANCEL
        
        route = get_start_end_location.loop(Fore.LIGHTCYAN_EX + ' Input start and end destination: ')
        if route == CANCEL:
            return CANCEL
      
        customer = get_customer_info.loop(Fore.LIGHTCYAN_EX + ' Input customer email address: ')
        if customer == CANCEL:
            return CANCEL
        
        package = self._app_data.create_delivery_package(weight, route, customer)
        
        return weight, route, customer, package
        
        
    def validate_route(self, route, new_route):
        while True:
            try:
                start_location, end_location = route
                if start_location not in new_route or end_location not in new_route:
                    raise ValueError(Fore.RED + 'Invalid route for this package (type "cancel" to abort)')
                
                start_index = new_route.index(start_location)
                end_index = new_route.index(end_location)
                if start_index > end_index:
                    raise ValueError(Fore.RED + 'Invalid route for this package (type "cancel" to abort)')
                    
                return new_route
            except ValueError as err:
                print(err)
                new_route = input(Fore.LIGHTCYAN_EX + ' Input route stops: ')
                if new_route == CANCEL:
                    return CANCEL
                self.validate_route(route, new_route)
        
        
    def display_delivery_routes(self, valid_routes):
        output = []
        for route in valid_routes:
            output.append(str(route))
        
        return 'Suitable delivery routes for this package: \n' + '\n'.join(output)
    
    
    def create_route(self, route):
        get_route = CreateRoute(self._app_data)
        msg = Fore.LIGHTCYAN_EX + 'No available delivery routes at the time, please create a new one!\n Input delivery route stops: '
        
        new_route = get_route.loop(msg)
        validated_route = self.validate_route(route, new_route)
        if validated_route == CANCEL:
            return OPERATION_CANCELLED
        
        departure_time = 'Jul 12 2024 18:30h'
        new_route = self._app_data.calculate_route_times(departure_time, validated_route)
        return new_route
        
    
    def select_route(self, valid_routes):
        get_id = GetId(self._app_data)        
        route_id = get_id.loop(Fore.LIGHTCYAN_EX + ' Select route (input route ID): ')
        if route_id == CANCEL:
            return OPERATION_CANCELLED
        return route_id    
        
    
