from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from models.employee_roles import EmployeeRoles
from colorama import Fore
from date_time.date_time_functionalities import DateTime


class ViewRoutesInProgress(BaseCommand):
    def __init__(self, params: list, app_data: AppData):
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data=app_data)
    
    def execute(self):
        super().execute()
        if not self._app_data.logged_in_employee.role == EmployeeRoles.MANAGER:
            raise ValueError(Fore.RED + 'Only managers can view information about routes in progress!') 
        
        date = DateTime.create_time_stamp_for_today()
        self._app_data.update_all_routes_status(date)
        
        routes_in_progress = self._app_data.get_routes_in_progress()
        return '\n'.join(routes_in_progress) if routes_in_progress else Fore.YELLOW + 'No routes in progress'
    
    def _requires_login(self) -> bool:
        True