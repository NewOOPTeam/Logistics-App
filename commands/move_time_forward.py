from date_time.date_time_functionalities import DateTime
from commands.base_command import BaseCommand
from core.application_data import AppData
from models.employee_roles import EmployeeRoles
from commands.interaction_loops.get_id import GetId
from colorama import Fore


class MoveTimeForward(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        self._params = params
        self._app_data = app_data

    def execute(self):
        super().execute()
        if not self._app_data.logged_in_employee.role == EmployeeRoles.MANAGER:
            raise ValueError(Fore.RED + 'Only managers can move time forward!')
        
        time = DateTime.future_date()
        
        get_id = GetId(self._app_data)        
        id = get_id.loop(Fore.LIGHTCYAN_EX + ' Select route to view (input route ID): ')
        route = self._app_data.get_route_by_id(id)    
        
        route.update_route_status(time)

        return route
    