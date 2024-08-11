from commands.interaction_loops.base_loop import BaseLoop
from core.application_data import AppData


class GetCustomerInfo(BaseLoop):
    def __init__(self, app_data: AppData) -> None:
        super().__init__(app_data)
        
    def helper(self, param):
        return self._app_data.find_customer_by_email(param)