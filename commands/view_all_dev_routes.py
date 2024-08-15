from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from models.employee_roles import EmployeeRoles
from colorama import Fore


class ViewAllDevRoutes(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)
    
    def execute(self):
        super().execute()
        if not self._app_data.logged_in_employee.role == EmployeeRoles.MANAGER:
            raise ValueError(Fore.RED + 'Only managers can view information about all delivery routes!')
        
        ## twa da e samo za routes in progress:
        # A manager at the company uses the system to find information about all delivery routes in progress. The system responds with information that contains each route’s stops, delivery weight, and the expected current stop based on the time of the day.
        
        route = self._app_data.view_all_delivery_routes() #promqna 16;55
        return route

    def _requires_login(self) -> bool:
        return True