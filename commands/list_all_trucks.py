from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from colorama import Fore


class ListAllTrucks(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)
    
    def execute(self):
        super().execute()
                
        list_trucks = self._app_data.list_all_trucks() 
        return list_trucks

    def _requires_login(self) -> bool:
        return True