from core.command_factory import CommandFactory
from commands.constants.constants import WELCOMING_MESSAGE
from commands.interaction_loops.login import Login
from core.application_data import AppData


class Engine:
    def __init__(self, factory: CommandFactory) -> None:
        self._factory = factory
        self._app_data = AppData()
        
    def start(self):
        output = []
        try:
            login = Login(self._app_data)
            login.loop()
        except ValueError as error:
            print(error)
            output.append(error.args[0])
        
        
        print(WELCOMING_MESSAGE)
        while (input_line := input(' Enter application command: \n').strip()):
            try:
                command = self._factory.create(input_line)
                user_output = command.execute()
                print(user_output)
                output.append(user_output)
            except Exception as error:
                print(error)
                output.append(error.args[0])
                
        print('\n'.join(output))