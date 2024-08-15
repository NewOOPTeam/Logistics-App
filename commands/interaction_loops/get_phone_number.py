from commands.interaction_loops.base_loop import BaseLoop
from commands.helper_methods import Validate
from colorama import Fore


class GetCustomerPhone(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
        
    def helper(self, param):
        Validate.str_len(param, 8, 13)
        if param[0] == '+':
            if not param[1:].isnumeric():
                raise ValueError(Fore.RED + 'Invalid phone number')
        return param