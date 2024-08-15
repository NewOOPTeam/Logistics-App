from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate
from models.employee_roles import EmployeeRoles
from colorama import Fore

class AddEmployee(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 3, self.__class__.__name__)
        super().__init__(params, app_data)
    
    def execute(self):
        super().execute()
        if self._app_data.logged_in_employee.role != EmployeeRoles.ADMIN:
            raise ValueError(Fore.RED + 'You need to be an administrator to perform this command.')
        
        firstname, lastname, role = self._params
        
        employee = self._app_data.add_employee(firstname, lastname, role)
        
        return Fore.GREEN + f'Employee {employee.firstname} {employee.lastname} added as {employee.role}'
    
    def _requires_login(self) -> bool:
        return True