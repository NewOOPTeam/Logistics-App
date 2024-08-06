from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate, Parse
from csv_file.distance_calculator import DistanceCalculator


class CreateDeliveryRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)
        
    def execute(self):
        while True:
            id = self.get_id()
            
            package = self.assign_package(id)
            if package:
                break
            
        if package == 'cancel':
            return
                    
        calc = DistanceCalculator()                    
        route_input = input(" Enter your route: ")
        distance = calc.get_route_distance(route_input)

        print(f'Route for package {id} created: {''.join(route_input)}, {calc}')
        return f'Route for package {id} created'
    
    
    def get_id(self):
        while (id := input(' Input package ID\n ')):
            try:
                id = Parse.to_int(id)
                return id
            except ValueError:
                print('Invalid ID')   
    
    def assign_package(self, id):
        try:
            package = self._app_data.find_package_by_id(id) 
            return package             
        except ValueError:
            print(f'Package with {id} not found')
            input_message = "Do you want to try another ID or cancel? (enter 'retry' or 'cancel'): "
            
            if (action := input(input_message).strip().lower()) == 'cancel':
                print("Operation cancelled.")
                return 'cancel'
            return None
