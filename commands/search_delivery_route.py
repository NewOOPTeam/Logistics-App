from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from commands.interaction_loops.get_id import GetId
from colorama import Fore
from date_time.date_time_functionalities import DateTime
from models.delivery_route import COMPLETED


class SearchRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)
    
    def execute(self):
        super().execute()
        
        get_id = GetId(self._app_data)        
        id = get_id.loop(Fore.LIGHTCYAN_EX + ' Select route to view (input route ID): ')
        route = self._app_data.get_route_by_id(id)        
        if DateTime.create_time_stamp_for_today() <= self.arrival_time:
            route.complete_route()
        
        return route if route._status != COMPLETED else 'Route is completed'

    def _requires_login(self) -> bool:
        return True