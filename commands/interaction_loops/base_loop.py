from core.application_data import AppData
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from commands.helper_methods import AcceptInput


class BaseLoop:
    def __init__(self, app_data: AppData) -> None:
        self._app_data = app_data
        
    def loop(self, msg):
        while True:
            param = self.get_input(msg)
            if param:
                break
        if param == CANCEL:
            return OPERATION_CANCELLED
        return param
            
            
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