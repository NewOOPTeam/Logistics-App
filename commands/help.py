from core.application_data import AppData
from commands.base_command import BaseCommand
from commands.helper_methods import Validate
from commands.constants.constants import DESCRIPTION_MESSAGE


class Help(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)


    def execute(self):
        return DESCRIPTION_MESSAGE
    
    def _requires_login(self) -> bool:
        return False