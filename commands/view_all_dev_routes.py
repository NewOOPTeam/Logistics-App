from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from models.employee_roles import EmployeeRoles
from colorama import Fore
from date_time.date_time_functionalities import DateTime


class ViewAllDevRoutes(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)
    
    def execute(self):
        super().execute()
        if not self._app_data.logged_in_employee.role == EmployeeRoles.MANAGER:
            raise ValueError(Fore.RED + 'Only managers can view information about all delivery routes!')
        
        date = DateTime.create_time_stamp_for_today()
        self._app_data.update_all_routes_status(date)
        routes = self._app_data.view_all_delivery_routes()
 
        return routes


    def _requires_login(self) -> bool:
        return True