from commands.interaction_loops.base_loop import BaseLoop
from commands.interaction_loops.get_username import GetUsername
from commands.interaction_loops.get_password import GetPassword
from core.application_data import AppData
from commands.constants.constants import INITIAL_LOGIN_CANCELLED, LOGIN_MESSAGE, CANCEL
from colorama import Fore


class Login(BaseLoop):
    def __init__(self, app_data: AppData) -> None:
        super().__init__(app_data)
        
    def loop(self):       
        print(LOGIN_MESSAGE)
        
        get_username = GetUsername(self._app_data)
        username = get_username.loop(Fore.LIGHTCYAN_EX + ' Enter username: ')
        
        if username == CANCEL:
            self.exit_system(INITIAL_LOGIN_CANCELLED)
        
        user = self._app_data.find_employee_by_username(username)

        get_password = GetPassword(self._app_data)
        password = get_password.loop(Fore.LIGHTCYAN_EX + ' Enter password: ', user)
        
        if password == CANCEL:
            self.exit_system(INITIAL_LOGIN_CANCELLED)
        
        self._app_data.login(user)
        self.enter_system(username)