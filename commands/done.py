from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.interaction_loops.base_loop import BaseLoop
from commands.constants.constants import EXIT_MESSAGE


class Done(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        super().__init__(params, app_data)

    def execute(self):
        exit = BaseLoop(self._app_data)
        exit.exit_system(EXIT_MESSAGE)