from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate, Parse
from csv_file.distance_calculator import DistanceCalculator as dc


class CreateDeliveryRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)
        
    def execute(self):
        id = input(' Input package ID\n ')
        id = Parse.to_int(id)
        package = self._app_data.find_package_by_id(id)
        if not package:
            print(f'Package with {id} not found')
        
        stops = []
                    
        number_of_stops = Parse.to_int(input(' Input number of stops: \n'))
        for _ in range(number_of_stops):
            stops.append(input())
        
        route = ' '.join(stops)
        
        distance = dc.get_route_distance(route)
        
        # start_location = package._start_location
        # end_location = package._end_location
        
        print(f'Route for package {id} created: {route}, overall distance: {distance}')
        return f'Route for package {id} created'