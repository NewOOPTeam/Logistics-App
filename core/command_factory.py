from commands.create_package import CreatePackage
from commands.create_delivery_route import CreateDeliveryRoute
from commands.search_delivery_route import SearchRoute
from commands.add_customer import AddCustomer
from commands.add_employee import AddEmployee
from commands.help import Help
from commands.view_package import ViewPackage
from commands.view_all_packages import ViewAllPackages
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand



class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line: str):
        command, *params = input_line.split()
                
        match command.lower():
            # case 'addemployee':
            #     return AddEmployee(params, self._app_data)
            case 'login':
                return LoginCommand(params, self._app_data)
            case 'logout':
                return LogoutCommand(self._app_data)
            case 'help':
                return Help(params, self._app_data)
            case 'createpackage':
                return CreatePackage(params, self._app_data)
            case 'addcustomer':
                return AddCustomer(params, self._app_data)
            case 'viewpackage':
                return ViewPackage(params, self._app_data)
            case 'viewallpackages':
                return ViewAllPackages(params, self._app_data)
            case 'createdeliveryroute':
                return CreateDeliveryRoute(params, self._app_data)
            case 'viewunassignedpackages':
                pass
            case 'searchroute':
                pass
            case 'viewdeliveryroute':
                pass
            case 'viewactiveroutes':
                pass
            case 'viewavailabletrucks':
                pass
            case 'assigntruck':
                pass
            case _:
                raise ValueError(f"Unknown command: '{command}'")