from colorama import Fore, Back, Style


CANCEL = 'cancel'
OPERATION_CANCELLED = Fore.YELLOW + 'Operation cancelled, returning to main menu'
INITIAL_LOGIN_CANCELLED = Fore.RED + 'Login cancelled, exiting program...'

WELCOMING_MESSAGE = Fore.LIGHTBLUE_EX + """
╔══════════════════════════════════╗
║     WELCOME TO ROUTE MASTER      ║
║                                  ║
║      Plan. Track. Deliver.       ║                                  
╚══════════════════════════════════╝
"""

DESCRIPTION_MESSAGE = Fore.LIGHTCYAN_EX + """
====================================================================
                      SYSTEM ACCESS GUIDE
====================================================================
You need to be logged in as either EMPLOYEE, MANAGER, SUPERVISOR, or
                    in order to use the system.
====================================================================

As an Employee, you are able to:
  - **Add Customer** to the system
  - **Create Package** for an existing customer. You will be able to 
  assign it to a suitable delivery route, or create a new delivery
  route.
  - **Create Delivery Route** to create a new delivery route
  - **Assign Truck To Route** to trigger the delivery process for a
  specified departure date.
  - **View Package** upon request to check its status, assigned route, 
    and the customer linked to it.
  - **View All Packages** to display information about all packages
  in the system
  - **List All Trucks** to see all available trucks.

As a Supervisor, you have access to:
  - **View Unassigned Packages** which responds with a list of 
  unassigned packages containing their IDs and locations.

As a Manager, you can:
  - **View All Delivery Routes** to see information about all delivery
  routes.
  - **View Routes In Progress** to find information about all
  delivery routes in progress. The system responds with each route's
  stops, delivery weight, and the expected current stop based on 
  the time of day.
  
  
- Type HELP to see this message again.
- Type DONE to exit program.

====================================================================

"""

LOGIN_MESSAGE = Fore.YELLOW + 'Please login in order to use the system'
EXIT_MESSAGE = Fore.RED + 'Shutting program down...'

COMPLETED = 'Completed'