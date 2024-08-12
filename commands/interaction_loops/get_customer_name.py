from commands.interaction_loops.base_loop import BaseLoop
from commands.helper_methods import Validate

class GetCustomerName(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
        
    def helper(self, param):
        Validate.str_len(param, 4, 10)
        return param