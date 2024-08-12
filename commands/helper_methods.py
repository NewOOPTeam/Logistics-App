from commands.constants.constants import CANCEL
from colorama import Fore


class Validate:
    @staticmethod
    def str_len(val, min, max):
        if not min <= len(val) <= max:
            raise ValueError(Fore.RED + 'Invalid parameter lenght')

    @staticmethod
    def params_count(params: list[str], count: int, cmd_name: str):
        if len(params) != count:
            raise ValueError(Fore.RED + f'{cmd_name} command expects {count} parameters.')


class Parse:
    @staticmethod
    def to_int(val):
        try:
            return int(val)
        except ValueError:
            raise ValueError(Fore.RED + 'Invalid number')
    
    @staticmethod
    def to_float(val):
        try:
            val = float(val)
            if val <= 0:
                raise ValueError(Fore.RED + "Value must be greater than zero.")
            return float(val)
        except ValueError:
            raise ValueError(Fore.RED + 'Invalid number')


class AcceptInput:
    @staticmethod
    def retry_or_cancel(input_message):
        if (action := input(input_message).strip().lower()) != 'cancel':
            return None
        return CANCEL