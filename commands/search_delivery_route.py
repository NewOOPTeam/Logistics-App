from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate


class SearchRoute(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 1, self.__class__.__name__)
        super().__init__(params, app_data)
    
    def execute(self):
        pass
        # possibly will use package ID
        
        # Search for a route based on package’s start and end locations.
        
        # Updating a delivery route – assign a free truck to it.
        # Updating a delivery route – assign a delivery package.
