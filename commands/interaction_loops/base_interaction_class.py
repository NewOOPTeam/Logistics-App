import sys
import time
from core.application_data import AppData


class BaseLoop:
    
    def __init__(self, app_data: AppData) -> None:
        self._app_data = app_data

    def enter_system(self, username):
        print(f'Employee {username} successfully logged in')
        print('Loading system...')
        time.sleep(1)

    def exit_system(self, msg):
        print(msg)
        time.sleep(1)
        sys.exit()