from core.command_factory import CommandFactory

class Engine:
    def __init__(self, factory: CommandFactory) -> None:
        self._factory = factory
        
    def start(self):
        output = []

        while (input_line := input().strip()) and input_line.lower() != 'done':
            try:
                command = self._factory.create(input_line)
                output.append(command.execute())
            except Exception as error:
                output.append(error.args[0])
                
        print('\n'.join(output))