from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from models.delivery_route import DeliveryRoute
from models.locations import Locations
from commands.interaction_loops.get_start_end_location import GetStartEndLocation
from colorama import Fore


class SearchRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 1, self.__class__.__name__)
        super().__init__(params, app_data)
    
    def execute(self):
        # start_location, end_location = GetStartEndLocation(self._app_data).loop(Fore.LIGHTCYAN_EX + ' Input start and end point: ')
        id = self._params[0]
        route = self._app_data.find_route_by_id(id)
        
        return route
        # check if truck on the route has capacity -> bool (from app data)
        # DATES
        # prefer to assign smallest capacity truck
