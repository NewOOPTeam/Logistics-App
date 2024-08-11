from commands.interaction_loops.base_loop import BaseLoop
from commands.helper_methods import Parse



class GetWeight(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
    
    def helper(self, param):
        return Parse.to_float(param)