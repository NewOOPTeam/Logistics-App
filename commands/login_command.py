from commands.base_command import BaseCommand
from core.application_data import AppData


class LoginCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        super().__init__(params, app_data)

    def execute(self):
        if self._app_data.has_logged_in_employee:
            logged_employee = self._app_data.logged_in_employee
            raise ValueError(f'Employee {logged_employee.username} is already logged in! Please log out first.')

        if len(self._params) != 2:
            raise ValueError('Incorrect number of parameters. Expected 2.')

        username, password = self._params

        try:
            employee = self._app_data.find_employee_by_username(username)
        except ValueError:
            raise ValueError('Employee not found!')

        if employee.password != password:
            raise ValueError('Wrong username or password!')

        self._app_data.login(employee)
        return f'Employee {employee.username} successfully logged in!'
    
    def _requires_login(self) -> bool:
        return False
