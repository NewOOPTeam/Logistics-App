from commands.helper_methods import Parse, AcceptInput
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from commands.interaction_loops.base_interaction_class import BaseLoop
from csv_file.distance_calculator import DistanceCalculator


class InputRoute(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
    
    def loop(self, msg):
        while True:
            route = self.get_route(msg)
            if route:
                break
        if route == CANCEL:
            return OPERATION_CANCELLED
    
     
    def get_route(self, msg):
        calc = DistanceCalculator()
        route_input = input(msg)
        try:
            route = route_input.strip().split()
            calc.validate_route(route)
            return tuple(route)
        except ValueError as err:
            print(err)
            input_message = "Do you want to retry or cancel? (input 'cancel' to abort): "
            AcceptInput.retry_or_cancel(input_message)
