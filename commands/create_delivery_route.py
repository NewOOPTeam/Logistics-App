from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate, Parse, AcceptInput
from csv_file.distance_calculator import DistanceCalculator
from date_time.date_time_functionalities import DateTime
from commands.constants.constants import CANCEL, OPERATION_CANCELLED


class CreateDeliveryRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)
        
    def execute(self):
        ################### UNFINISHED #####################

        # Creating a delivery route – should have a unique id, and a list of locations (at least two).
        # datetime
        # expected delivery date
        # route needs to be assigned an ID, so we need to create a DeliveryRoute class
        
        # The first location is the starting location – it has a departure time.
        # The other locations have expected arrival time.

        while True:
            id = self.get_id()
            package = self.find_package(id)
            if package:
                break
        if package == CANCEL:
            return OPERATION_CANCELLED
                    
                    
        while True:
            route = self.get_route()
            if route:
                break
        if route == CANCEL:
            return OPERATION_CANCELLED
        
        # package ID
        # route
        
        

        # return f'Route for package ID{id} created: {''.join(route_input)}, {calc}'
    
    
    
    def get_id(self):
        while (id := input(' Input package ID\n ')):
            try:
                id = Parse.to_int(id)
                return id
            except ValueError:
                print('Invalid ID') 
    
    def get_route(self):
        calc = DistanceCalculator()                    
        route_input = input(" Enter your route: ")
        try:
            route = route_input.strip().split()
            calc.validate_route(route)
            return tuple(route)
        except ValueError as err:
            print(err)
            input_message = "Do you want to retry or cancel? (input 'cancel' to abort): "
            AcceptInput.retry_or_cancel(input_message)
    
    def find_package(self, id):
        try:
            package = self._app_data.find_package_by_id(id) 
            return package             
        except ValueError:
            print(f'Package with ID {id} not found')
            input_message = "Do you want to try another ID? (input 'cancel' to abort): "
            AcceptInput.retry_or_cancel(input_message)
            
    def get_start_date(self):
        pass