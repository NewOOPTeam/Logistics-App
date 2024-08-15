from commands.interaction_loops.base_loop import BaseLoop
from commands.helper_methods import Parse
from Vehicles.truck_class_model import TruckConstants


class GetWeight(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
    
    def helper(self, param):
        param = Parse.to_float(param)
        if param > TruckConstants.SCANIA_CAPACITY:
            raise ValueError('Cannot assign package to any truck')
        return param