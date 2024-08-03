from core.application_data import AppData
from commands.base_command import BaseCommand

class AddCustomer(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        super().__init__(params, app_data)

    def execute(self):
        firstname, lastname, phone_number, email = self._params
        customer = self._app_data.add_customer(firstname, lastname, phone_number, email)
        
        return f'User {customer.firstname} {customer.lastname} added'
        