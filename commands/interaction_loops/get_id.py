from commands.interaction_loops.base_loop import BaseLoop
from commands.helper_methods import Parse



class GetId(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
    
    def helper(self, msg):
        while (id := input(msg)):
            try:
                id = Parse.to_int(id)
                return id
            except ValueError:
                print('Invalid ID')