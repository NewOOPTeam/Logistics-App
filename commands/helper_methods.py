from commands.constants.constants import CANCEL


class Validate:
    @staticmethod
    def str_len(val, min, max):
        if not min <= len(val) <= max:
            raise ValueError('Invalid input')

    @staticmethod
    def params_count(params: list[str], count: int, cmd_name: str):
        if len(params) != count:
            raise ValueError(f'{cmd_name} command expects {count} parameters.')


class Parse:
    @staticmethod
    def to_int(val):
        try:
            return int(val)
        except:
            raise ValueError()
    
    @staticmethod
    def to_float(val):
        try:
            val = float(val)
            if val <= 0:
                raise ValueError("Value must be greater than zero.")
            return float(val)
        except:
            raise ValueError('Invalid number')


class AcceptInput:
    @staticmethod
    def retry_or_cancel(input_message):
        if (action := input(input_message).strip().lower()) != 'cancel':
            return None
        return CANCEL