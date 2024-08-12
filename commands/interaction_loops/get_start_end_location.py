from commands.interaction_loops.base_loop import BaseLoop
from csv_file.distance_calculator import DistanceCalculator
from commands.helper_methods import Validate


class GetStartEndLocation(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
    
    def helper(self, param):
        calc = DistanceCalculator()
        route = param.strip().split()
        calc.validate_route(route)
        Validate.params_count(list(route), 2, '')
        return tuple(route)
