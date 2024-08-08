from commands.helper_methods import Parse, AcceptInput
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from commands.interaction_loops.base_interaction_class import BaseLoop


class FindPackage(BaseLoop):
    
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
    
    def loop(self):
        while True:
            id = self.get_id()
            package = self.find_package(id)
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