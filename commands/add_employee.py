from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate


class AddEmployee(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 3, self.__class__.__name__)
        super().__init__(params, app_data)
    
    def execute(self):
        firstname, lastname, role = self._params
        
        employee = self._app_data.add_employee(firstname, lastname, role)
        
        return f'Employee {employee.firstname} {employee.lastname} added as {employee.role}'