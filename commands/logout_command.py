from commands.base_command import BaseCommand
from core.application_data import AppData
from colorama import Fore


class LogoutCommand(BaseCommand):
    def __init__(self, app_data: AppData):
        super().__init__(params=[], app_data=app_data)

    def execute(self):
        super().execute()
        self._app_data.logout()
        return Fore.YELLOW + 'You logged out!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0 

    def _execute(self):
        self._app_data.logout()
