from core.command_factory import CommandFactory
from commands.constants.constants import WELCOMING_MESSAGE

class Engine:
    def __init__(self, factory: CommandFactory) -> None:
        self._factory = factory
        
    def start(self):
        output = []
        print(WELCOMING_MESSAGE)
        while (input_line := input(' Enter application command: \n').strip()) and input_line.lower() != 'done':
            try:
                command = self._factory.create(input_line)
                user_output = command.execute()
                print(user_output)
                output.append(user_output)
            except Exception as error:
                output.append(error.args[0])
                
        print('\n'.join(output))