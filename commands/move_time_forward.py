from date_time.date_time_functionalities import DateTime
from commands.view_all_dev_routes import ViewAllDevRoutes
from commands.search_delivery_route import SearchRoute
from commands.base_command import BaseCommand
from core.application_data import AppData


class MoveTimeForward(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        self._params = params
        self._app_data = app_data

    def execute(self):
        time = DateTime.future_date()
        
        # routes = ViewAllDevRoutes(self._params, self._app_data).execute()
        route = SearchRoute(self._params, self._app_data).execute()

        return route
    