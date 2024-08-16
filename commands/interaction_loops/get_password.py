from commands.interaction_loops.base_loop import BaseLoop
from models.employee import Employee
from commands.constants.constants import CANCEL
from colorama import Fore


class GetPassword(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
        
    def loop(self, msg, user):
        while True:
            password = self.helper(msg, user)
            if password:
                return password
    
    def helper(self, msg, employee: Employee):
        try:
            password = input(msg)
            if password.lower() == CANCEL:
                return CANCEL
            
            if password != employee.password:
                raise ValueError(Fore.RED + 'Invalid password, retry or enter "cancel"')
            return password
        except ValueError as err:
            print(err)