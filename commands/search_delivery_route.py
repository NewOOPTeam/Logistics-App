from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from models.delivery_route import DeliveryRoute
from models.locations import Locations
from commands.interaction_loops.find_route import InputRoute



class SearchRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 2, self.__class__.__name__)
        super().__init__(params, app_data)
    
    def execute(self):
        start_location, end_location = InputRoute(self._app_data).loop(' Input start and end point: ')
        
        