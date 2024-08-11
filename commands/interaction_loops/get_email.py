from commands.interaction_loops.base_loop import BaseLoop
from commands.helper_methods import Validate

class GetEmail(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
    
    def helper(self, param):
        Validate.str_len(param, 7, 20)
        if '@' not in param:
            raise ValueError('Invalid email address')
        if self._app_data.customer_exists(param):
            raise ValueError(f'Customer with email {param} already exists')
        return param
            