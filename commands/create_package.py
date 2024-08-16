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
 
    def execute(self):
        super().execute()
        
        package_info = self.create_package()
   
        if package_info is None:
            return self.cancel_operation(None)
       
        weight, route, customer, package = package_info
       
        valid_routes = self._app_data.find_valid_routes_for_package(package.id)
        if valid_routes:
            routes = self.display_delivery_routes(valid_routes)
            print(routes)
            route_id = self.select_route(valid_routes)
            if route_id == CANCEL:
                return self.cancel_operation(package)
            new_route = self._app_data.get_route_by_id(route_id)
        else:
            new_route = self.create_route(route)
            if new_route == CANCEL:
                return self.cancel_operation(package)
           
        package = self._app_data.assign_package_to_route(package.id, new_route.id)
        message = (
                f'{Fore.GREEN}Delivery created for Package #{Fore.YELLOW}{package.id}{Fore.GREEN}, '
                f'assigned to route #{Fore.YELLOW}{new_route.id}{Fore.GREEN}:\n{Fore.RESET}'
                f'\n{new_route}\n\n'
                f'{Fore.YELLOW}Awaiting assignment to available truck.{Fore.RESET}'
            )
            
        return message

 
       
    def _requires_login(self) -> bool:
        return True
       
    def create_package(self):
        get_weight = GetWeight(self._app_data)
        get_start_end_location = GetStartEndLocation(self._app_data)
        get_customer_info = GetCustomerInfo(self._app_data)
 
        weight = get_weight.loop(Fore.LIGHTCYAN_EX + ' Input package weight: ')
        if weight == CANCEL:
            return None
       
        route = get_start_end_location.loop(Fore.LIGHTCYAN_EX + ' Input start and end destination: ')
        if route == CANCEL:
            return None
     
        customer = get_customer_info.loop(Fore.LIGHTCYAN_EX + ' Input customer email address: ')
        if customer == CANCEL:
            return None
       
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
                new_route = tuple(new_route.split(' '))
                if new_route == CANCEL:
                    return CANCEL
                return self.validate_route(route, new_route)
       
       
    def display_delivery_routes(self, valid_routes):
        output = []
        for route in valid_routes:
            output.append(str(route))
       
        return 'Suitable delivery routes for this package: \n' + '\n'.join(output)
   
   
    def create_route(self, route):
        get_route = CreateRoute(self._app_data)
        msg = Fore.RED + 'No available delivery routes at the time, please create a new one!\n' + Fore.LIGHTCYAN_EX + ' Input delivery route stops: '
       
        new_route = get_route.loop(msg)
        validated_route = self.validate_route(route, new_route)
        if validated_route == CANCEL:
            return CANCEL
        
        departure_time = input(Fore.LIGHTCYAN_EX + ' Input departure time: ')
        
        new_route = self._app_data.create_delivery_route(validated_route, departure_time)
        return new_route
       
   
    def select_route(self, valid_routes):
        get_id = GetId(self._app_data)        
 
        selected_route_id = get_id.loop(Fore.LIGHTCYAN_EX + ' Select route (input route ID): ')
        route_ids = [route.id for route in valid_routes]
        if selected_route_id == CANCEL:
            return CANCEL
       
        try:
            if selected_route_id not in route_ids:
                raise ValueError(Fore.RED + 'Please select one of the displayed routes!')
            return selected_route_id
        except ValueError as err:
            print(err)
            return self.select_route(valid_routes)    
       
       
    def cancel_operation(self, package):
        if package:
            self._app_data._delivery_packages.remove(package)
        return OPERATION_CANCELLED