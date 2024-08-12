from commands.interaction_loops.base_loop import BaseLoop
from commands.constants.constants import CANCEL
from colorama import Fore

class GetUsername(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
    
    def loop(self, msg):
        while True:
            username = self.helper(msg)
            if username:
                return username
            
    def helper(self, msg):
        try:
            username = input(msg)
            if username.lower() == CANCEL:
                return CANCEL
            
            if not self._app_data.user_exists(username):
                raise ValueError(Fore.RED + 'Wrong username, retry or enter "cancel"')
            return username  
        except ValueError as err:
            print(err)