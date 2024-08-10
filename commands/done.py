from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.interaction_loops.base_interaction_class import BaseLoop


class Done(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        super().__init__(params, app_data)

    def execute(self):
        exit = BaseLoop()
        exit.exit_system('Shutting program down...')