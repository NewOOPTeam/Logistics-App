from commands.assign_package_to_route import AssignPackageToRoute
from commands.assign_truck_to_route import AssignTruckToRoute
from commands.create_package import CreatePackage
from commands.create_delivery_route import CreateDeliveryRoute
from commands.move_time_forward import MoveTimeForward
from commands.search_delivery_route import SearchRoute
from commands.add_customer import AddCustomer
from commands.create_delivery import CreateDelivery
from commands.view_unassigned_packages import ViewUnassignedPackages
from commands.help import Help
from commands.view_all_dev_routes import ViewAllDevRoutes
from commands.view_package import ViewPackage
from commands.view_all_packages import ViewAllPackages
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand
from commands.done import Done
from colorama import Fore
from date_time.date_time_functionalities import DateTime
from commands.list_all_trucks import ListAllTrucks



class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line: str):
        command, *params = input_line.split()
        ## since we dont use params anywhere, we could remove them so that the commands can be input as normal words like "add delivery route"
                
        match command.lower().replace(' ', ''):
            # case 'addemployee':
            #     return AddEmployee(params, self._app_data)
            case 'login':
                return LoginCommand(params, self._app_data)
            case 'logout':
                return LogoutCommand(self._app_data)
            case 'help':
                return Help(params, self._app_data)
            case 'addcustomer':
                return AddCustomer(params, self._app_data)
            case 'createpackage':
                return CreatePackage(params, self._app_data)
            case 'viewpackage':
                return ViewPackage(params, self._app_data)
            case 'viewallpackages':
                return ViewAllPackages(params, self._app_data)
            case 'createdeliveryroute': # moje da go obedinim s createdelivery 
                return CreateDeliveryRoute(params, self._app_data)
            case 'createdelivery': # maikata - tuk vliza assign truck - vij notes
                return CreateDelivery(params, self._app_data)
            case 'assignpackagetoroute':# moje da go obedinim s createdelivery 
                return AssignPackageToRoute(params, self._app_data)
            case 'viewunassignedpackages': # da se razpishe
                return ViewUnassignedPackages(params, self._app_data)
            case 'viewdeliveryroute': #?? Davam ID i listva pratkite.kg i destinaciite
                return SearchRoute(params, self._app_data)
            case 'viewalldeliveryroutes': #?? Davam ID i listva pratkite.kg i destinaciite
                return ViewAllDevRoutes(params, self._app_data)#promqna 16;55
            case 'viewroutesinprogress':
                pass # da se razpishe
            case 'assigntrucktoroute':
                return AssignTruckToRoute(params, self._app_data)
            case 'timeforward':
                return MoveTimeForward(DateTime)
            case 'listalltrucks':
                return ListAllTrucks(params, self._app_data)
            case 'done':
                return Done(params, self._app_data)
            case _:
                raise ValueError(Fore.RED + f"Unknown command: '{command}'")
