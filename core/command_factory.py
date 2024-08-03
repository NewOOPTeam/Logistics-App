
class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line: str):
        cmd_name, *params = input_line.split()