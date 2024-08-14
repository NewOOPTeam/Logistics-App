from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from commands.interaction_loops.get_id import GetId
from colorama import Fore


class SearchRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)
    
    def execute(self):
        # start_location, end_location = GetStartEndLocation(self._app_data).loop(Fore.LIGHTCYAN_EX + ' Input start and end point: ')
        get_id = GetId(self._app_data)        
        id = get_id.loop(Fore.LIGHTCYAN_EX + ' Select route to view (input route ID): ')
        route = self._app_data.get_route_by_id(id)        
        
        return route
        # check if truck on the route has capacity -> bool (from app data)
        # DATES
        # prefer to assign smallest capacity truck
