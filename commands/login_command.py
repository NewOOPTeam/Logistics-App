from commands.base_command import BaseCommand
from core.application_data import AppData
from colorama import Fore
from commands.interaction_loops.login import Login


class LoginCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        super().__init__(params, app_data)

    def execute(self):
        self._throw_if_user_logged_in()

        login = Login(self._app_data)
        user = login.loop()

        return Fore.GREEN + f'Employee {user.username} successfully logged in!'
    
    def _requires_login(self) -> bool:
        return False
