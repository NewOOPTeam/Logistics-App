from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from commands.interaction_loops.get_id import GetId
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from colorama import Fore


class ViewPackage(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)
        
    def execute(self):
        super().execute()
        
        get_id = GetId(self._app_data)
        id = get_id.loop(Fore.LIGHTCYAN_EX + ' Input package ID: ')

        if id == CANCEL:
            return OPERATION_CANCELLED
        
        package = self._app_data.find_package_by_id(id)            
        return str(package)
    
    def _requires_login(self) -> bool:
        return True