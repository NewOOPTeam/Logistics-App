# from models.delivery_package import DeliveryPackage
# from commands.helper_methods import Validate, Parse, AcceptInput
# from commands.constants.constants import CANCEL, OPERATION_CANCELLED



class BaseLoop:
    
    def __init__(self, app_data) -> None:
        self.app_data = app_data


    def loop(self):
        pass