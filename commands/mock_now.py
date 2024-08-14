from date_time.date_time_functionalities import DateTime
from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate


class MockNowCommand:
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 1, self.__class__.__name__)
        super().__init__(params, app_data)
        self.params = params

    def execute(self):
        DateTime.mock_now(self._params[0])

