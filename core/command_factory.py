from commands.add_package import AddPackage
from commands.create_delivery_route import CreateDeliveryRoute
from commands.add_customer import AddCustomer
from commands.add_employee import AddEmployee
from commands.view_package import ViewPackage

class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line: str):
        command, *params = input_line.split()


        #### APPLICATION FUNCTIONALITIES ####
        # Creating a delivery route – should have a unique id, and a list of locations (at least two).
        # The first location is the starting location – it has a departure time.

        # The other locations have expected arrival time.

        # Search for a route based on package’s start and end locations.

        # Updating a delivery route – assign a free truck to it.

        # Updating a delivery route – assign a delivery package.

        # View a information about routes, packages and trucks.

        
        match command.lower():
            case 'addemployee':
                return AddEmployee(params, self._app_data)
            case 'addcustomer':
                return AddCustomer(params, self._app_data)
            case 'addpackage':
                return AddPackage(params, self._app_data)
            case 'viewpackage':
                return ViewPackage(params, self._app_data)
            case 'createdeliveryroute':
                return CreateDeliveryRoute(params, self._app_data)
            case 'viewdeliveryroute':
                pass
            case 'searchdeliveryroute':
                pass
            case _:
                raise ValueError(f"Unknown command: '{command}'")