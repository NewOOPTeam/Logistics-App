from commands.create_package import CreatePackage
from commands.add_customer import AddCustomer

class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line: str):
        command, *params = input_line.split()
        
        # An employee of the company must be able to record the details of a delivery package, create or search for suitable delivery routes, and inspect the current state of delivery packages, transport vehicles and delivery routes.
        
        # Creating a delivery package – unique id, start location, end location and weight in kg, and contact information for the customer.

        # Creating a delivery route – should have a unique id, and a list of locations (at least two).
        # The first location is the starting location – it has a departure time.

        # The other locations have expected arrival time.

        # Search for a route based on package’s start and end locations.

        # Updating a delivery route – assign a free truck to it.

        # Updating a delivery route – assign a delivery package.

        # View a information about routes, packages and trucks.
        
        if command.lower() == 'addcustomer':
            return AddCustomer(params, self._app_data)
        if command.lower() == 'createpackage':
            return CreatePackage(params, self._app_data)
        if command.lower() == 'viewpackage':
            pass
        if command.lower() == 'viewdeliveryroute':
            pass
        if command.lower() == 'createdeliveryroute':
            pass
        if command.lower() == 'searchdeliveryroute':
            pass