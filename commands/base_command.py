from core.application_data import AppData


class BaseCommand:
    def __init__(self, params: list[str], app_data: AppData) -> None:
        self._params = params
        self._app_data = app_data

    def execute(self):
        pass