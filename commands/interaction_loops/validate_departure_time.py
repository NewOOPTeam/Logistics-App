from commands.interaction_loops.base_loop import BaseLoop
from date_time.date_time_functionalities import DateTime
from commands.constants.constants import CANCEL

class ValidateDepartureTime(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
    
    def helper(self, param):
        date_dep_time = DateTime.date_from_string(param)
        departure_time = DateTime.string_from_date(date_dep_time)
        return departure_time