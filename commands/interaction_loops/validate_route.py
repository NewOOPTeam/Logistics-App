from commands.interaction_loops.base_loop import BaseLoop
from commands.constants.constants import CANCEL
from colorama import Fore
from commands.interaction_loops.create_route import CreateRoute
        

class ValidateRoute(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
    
    def loop(self, route, new_route):
        while True:
            try:
                route = self.helper(route, new_route)
                if new_route:
                    return new_route
            except ValueError as err:
                print(err)
            
    def helper(self, route, new_route):
        start_location, end_location = route
        
        if start_location not in new_route or end_location not in new_route:
            raise ValueError(Fore.RED + 'Invalid route for this package (type "cancel" to abort)')
        
        start_index = new_route.index(start_location)
        end_index = new_route.index(end_location)
        if start_index > end_index:
            raise ValueError(Fore.RED + 'Invalid route for this package (type "cancel" to abort)')
        return new_route  