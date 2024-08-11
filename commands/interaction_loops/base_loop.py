from core.application_data import AppData
from commands.constants.constants import CANCEL, WELCOMING_MESSAGE, DESCRIPTION_MESSAGE
from commands.helper_methods import AcceptInput
import sys
import time


class BaseLoop:
    def __init__(self, app_data: AppData) -> None:
        self._app_data = app_data
        
    def loop(self, msg):
        while True:
            param = self.get_input(msg)
            if param:
                break
        return param if param != CANCEL else CANCEL
            
            
    def get_input(self, msg):
        param = input(msg)
        try:
            param = self.helper(param)
            return param
        except ValueError as err:
            print(err)
            input_message = "Do you want to retry or cancel? (input 'cancel' to abort): "
            return AcceptInput.retry_or_cancel(input_message)
        
    def helper(self, param):
        pass
    
    def enter_system(self, username):
        print(f'Employee {username} successfully logged in')
        print('Loading system...')
        time.sleep(1)
        print(WELCOMING_MESSAGE)
        print(DESCRIPTION_MESSAGE)

    def exit_system(self, msg):
        print(msg)
        time.sleep(1)
        sys.exit()