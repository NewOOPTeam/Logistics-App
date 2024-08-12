from core.application_data import AppData
from commands.base_command import BaseCommand
from commands.helper_methods import Validate
from commands.interaction_loops.get_customer_name import GetCustomerName
from commands.interaction_loops.get_email import GetEmail
from commands.interaction_loops.get_phone_number import GetCustomerPhone
from commands.constants.constants import CANCEL, OPERATION_CANCELLED
from colorama import Fore


class AddCustomer(BaseCommand):
    def __init__(self, params: list[str], app_data: AppData) -> None:
        Validate.params_count(params, 0, self.__class__.__name__)
        super().__init__(params, app_data)

    def execute(self):
        
        get_name = GetCustomerName(self._app_data)
        get_email = GetEmail(self._app_data)
        get_phone = GetCustomerPhone(self._app_data)
        
        first_name = get_name.loop(Fore.LIGHTCYAN_EX + ' Input first name: ')
        if first_name == CANCEL:
            return OPERATION_CANCELLED
        
        last_name = get_name.loop(Fore.LIGHTCYAN_EX + ' Input last name: ')
        if last_name == CANCEL:
            return OPERATION_CANCELLED
        
        email = get_email.loop(Fore.LIGHTCYAN_EX + ' Input customer email: ')
        if email == CANCEL:
            return OPERATION_CANCELLED
        
        phone = get_phone.loop(Fore.LIGHTCYAN_EX + ' Input phone number: ')
        if phone == CANCEL:
            return OPERATION_CANCELLED
        
        try:
            customer = self._app_data.add_customer(first_name, last_name, phone, email)
        except:
            raise ValueError(Fore.RED + 'Unexpected error occurred')
        
        return Fore.GREEN + f'User {customer.firstname} {customer.lastname} added'
    
    def _requires_login(self) -> bool:
        return True
        