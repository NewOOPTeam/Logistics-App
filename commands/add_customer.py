from core.application_data import AppData
from commands.base_command import BaseCommand
from commands.helper_methods import Validate


class AddCustomer(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        super().__init__(params, app_data)

    def execute(self):
        firstname, lastname, phone_number, email = self._params
        Validate.str_len(firstname, 3, 100)
        Validate.str_len(lastname, 3, 100)
        customer = self._app_data.add_customer(firstname, lastname, phone_number, email)
        
        return f'User {customer.firstname} {customer.lastname} added'
        