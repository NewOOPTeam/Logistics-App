from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.interaction_loops.base_loop import BaseLoop
from commands.constants.constants import EXIT_MESSAGE


class Done(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        super().__init__(params, app_data)

    def execute(self):
        self._throw_if_user_logged_in()
        exit = BaseLoop(self._app_data)
        # self._app_data.save_state()
        exit.exit_system(EXIT_MESSAGE)
        
    def _requires_login(self) -> bool:
        return False