from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from commands.interaction_loops.find_route import InputRoute
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from date_time.date_time_functionalities import DateTime
from datetime import timedelta
from csv_file.distance_calculator import DistanceCalculator
from models.delivery_route import DeliveryRoute



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

        # package = FindPackage(self._app_data).loop(' Input package ID: ') - da premahnem package- da ostavim samo route
        # if package == OPERATION_CANCELLED:
        #     return OPERATION_CANCELLED

        route = InputRoute(self._app_data).loop(' Input delivery route stops: ')
        if route == OPERATION_CANCELLED:
            return OPERATION_CANCELLED
        # it should return arrival time from location to location when i have more than 2 locations


        # def get_arrival_time:
            # choice 1 - asap
            # choice 2 - input
        
        # package ID
        # route
        


    def calculate_route_times(self, route):
        if not route or len(route) < 2:
            raise ValueError("Route must have at least two locations.")

        starting_location = route[0]
        departure_time = DateTime.create_time_stamp_for_now()  # Assuming this returns a datetime object
        
        locations = route[1:]
        locations_dict = {}

        distance_calculator = DistanceCalculator()

        previous_location = starting_location
        previous_time = departure_time

        for location in locations:
            both_locations = [previous_location, location]
            distance = distance_calculator.calculate_total_distance(route=both_locations)
            travel_time = timedelta(hours=distance / 87)
        
            arrival_time = previous_time + travel_time
            locations_dict[location] = arrival_time
            
            print(f"Arrival at {location}: {arrival_time}")
            
            previous_location = location
            previous_time = arrival_time

        delivery_route = self._app_data.create_delivery_route(departure_time, arrival_time, locations_dict)
        
        return delivery_route



            
 
    def get_start_date(self):
        pass

