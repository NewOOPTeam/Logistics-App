from commands.base_command import BaseCommand
from core.application_data import AppData
from commands.helper_methods import Validate, Parse


class ViewPackage(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 1, self.__class__.__name__)
        super().__init__(params, app_data)
        
    def execute(self):
        id = self._params[0]
        id = Parse.to_int(id)
        
        package = self._app_data.find_package_by_id(id)
        return str(package)