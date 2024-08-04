from commands.create_package import CreatePackage
from commands.add_customer import AddCustomer

class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line: str):
        command, *params = input_line.split()
        
        
        #### EMPLOYEE ####
        # An employee of the company must be able to record the details of a delivery package, create or search for suitable delivery routes, and inspect the current state of delivery packages, transport vehicles and delivery routes.
        
        # Creating a delivery package – unique id, start location, end location and weight in kg, and contact information for the customer.


        #### APPLICATION FUNCTIONALITIES ####
        # Creating a delivery route – should have a unique id, and a list of locations (at least two).
        # The first location is the starting location – it has a departure time.

        # The other locations have expected arrival time.

        # Search for a route based on package’s start and end locations.

        # Updating a delivery route – assign a free truck to it.

        # Updating a delivery route – assign a delivery package.

        # View a information about routes, packages and trucks.
        #case match 
        
        match command.lower():
            case 'createemployee':
                pass
            case 'login':
                pass
            case 'addcustomer':
                return AddCustomer(params, self._app_data)
            case 'createpackage':
                return CreatePackage(params, self._app_data)
            case 'viewpackage':
                pass
            case 'createdeliveryroute':
                pass
            case 'viewdeliveryroute':
                pass
            case 'searchdeliveryroute':
                pass