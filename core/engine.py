from core.command_factory import CommandFactory

class Engine:
    def __init__(self, factory: CommandFactory) -> None:
        self._command_factory = factory
        
    def start(self):
        output = []

        while (input_line := input().strip().lower()) != 'exit':
            try:
                cmd = self._command_factory.create(input_line)
                output.append(cmd)
            except Exception as error:
                output.append(error.args[0])
                
        print('\n'.join(output))