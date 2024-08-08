from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate, AcceptInput
from date_time.date_time_functionalities import DateTime
from commands.interaction_loops.find_package import FindPackage
from commands.interaction_loops.find_route import FindRoute
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

        package = FindPackage(self._app_data).loop()
        if package == OPERATION_CANCELLED:
            return OPERATION_CANCELLED

        route = FindRoute(self._app_data).loop()
        if route == OPERATION_CANCELLED:
            return OPERATION_CANCELLED
        
        # def get_arrival_time:
            # choice 1 - asap
            # choice 2 - input
        
        # package ID
        # route
        
        
 
    def get_start_date(self):
        pass