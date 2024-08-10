from core.application_data import AppData



class BaseCommand:
    def __init__(self, params: list[str], app_data: AppData) -> None:
        self._params = params
        self._app_data = app_data

    def execute(self):
        if self._requires_login() and not self._app_data.has_logged_in_employee:
            raise ValueError('You are not logged in! Please login first!')
        
    def _requires_login(self) -> bool:
        return True
    
    def _throw_if_user_logged_in(self):
        if self._app_data.has_logged_in_employee:
            logged_employee = self._app_data.logged_in_employee
            raise ValueError(
                f'Employee {logged_employee.username} is logged in! Please log out first!')

    @property
    def params(self):
        return self._params

    @property
    def app_data(self):
        return self._app_data
