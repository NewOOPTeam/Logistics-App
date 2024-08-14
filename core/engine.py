from core.command_factory import CommandFactory
from commands.constants.constants import LOGIN_MESSAGE
from commands.interaction_loops.login import Login
from core.application_data import AppData
from colorama import Fore


class Engine:
    def __init__(self, factory: CommandFactory, app_data: AppData) -> None:
        self._factory = factory
        self._app_data = app_data
        
    def start(self):
        output = []
        # try:
        #     print(LOGIN_MESSAGE)
        #     login = Login(self._app_data)
        #     user = login.loop()
        #     login.enter_system(user.username)
        # except ValueError as error:
        #     print(error)
        #     output.append(error.args[0])

        while (input_line := input(Fore.LIGHTCYAN_EX + ' Enter application command: \n').strip()):
            try:
                command = self._factory.create(input_line)
                user_output = command.execute()
                print(user_output)
                output.append(user_output)
            except Exception as error:
                print(error)
                output.append(error.args[0])
                
        print('\n'.join(output))