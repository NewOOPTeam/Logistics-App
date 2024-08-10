from commands.interaction_loops.base_interaction_class import BaseLoop
from models.employee import Employee
from commands.constants.constants import CANCEL, LOGIN_MESSAGE



class Login(BaseLoop):
    def __init__(self, app_data) -> None:
        super().__init__(app_data)
        
    def loop(self):
        print(LOGIN_MESSAGE)
        
        while True:
            username = self.get_username()
            if username:
                break
        if username == CANCEL:
            self.exit_system('Command cancelled, exiting program.')            
            
        user = self.app_data.find_employee_by_username(username)
        
        while True:
            password = self.get_password(user)
            if password:
                break    
        if password == CANCEL:
            self.exit_system('Command cancelled, exiting program.')

        # self.app_data.logged_in_employee = user
        self.app_data.login(user)
        self.enter_system(username)        
    
    
            
    def get_username(self):
        try:
            username = input(' Enter username: ')
            if username.lower() == CANCEL:
                return CANCEL
            
            if not self.app_data.user_exists(username):
                raise ValueError('Wrong username, retry or enter "cancel"')
            return username  
        except ValueError as err:
            print(err)
            
    
    def get_password(self, employee: Employee):
        try:
            password = input(' Enter password: ')
            if password != employee.password:
                raise ValueError('Invalid password, retry or enter "cancel"')
            return password
        except ValueError as err:
            print(err)