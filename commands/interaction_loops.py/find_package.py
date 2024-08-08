from models.delivery_package import DeliveryPackage
from commands.helper_methods import Validate, Parse, AcceptInput
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from core.application_data import AppData



class FindPackage:
    
    def __init__(self, app_data: AppData) -> None:
        self.app_data = app_data

    @staticmethod
    def loop():
        while True:
            id = FindPackage.get_id()
            package = FindPackage.find_package(id)
            if package:
                break
        if package == CANCEL:
            return OPERATION_CANCELLED
        return package


    def get_id(self):
        while (id := input(' Input package ID\n ')):
            try:
                id = Parse.to_int(id)
                return id
            except ValueError:
                print('Invalid ID') 
                
    def find_package(self, id):
        try:
            package = self.app_data.find_package_by_id(id)
            return package             
        except ValueError:
            print(f'Package with ID {id} not found')
            input_message = "Do you want to try another ID? (input 'cancel' to abort): "
            AcceptInput.retry_or_cancel(input_message)