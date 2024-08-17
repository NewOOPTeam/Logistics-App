from core.application_data import AppData
from commands.base_command import BaseCommand
from commands.helper_methods import Validate
from models.employee_roles import EmployeeRoles
from colorama import Fore


class ViewUnassignedPackages(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)

    def execute(self):
        super().execute()
        
        if not self._app_data.logged_in_employee.role == EmployeeRoles.SUPERVISOR:
            raise ValueError(Fore.RED + 'Only supervisors can view all packages!')
        
        packages = self._app_data.find_unassigned_packages()
        
        return packages if packages else 'No unassigned packages at the moment.'
    
    def _requires_login(self) -> bool:
        True