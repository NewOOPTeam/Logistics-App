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
You need to be logged in as either ADMIN, MANAGER, SUPERVISOR, or
              EMPLOYEE in order to use the system.
====================================================================

As an Employee, you are able to:
  - **Create Package** for an existing customer or add a new customer
  to the database. You will be able to assign it for delivery right
  away or withhold delivery if no trucks are available.
  - **View Package** upon request to check its status, assigned route, 
    and the customer linked to it.
  - **Create Delivery** for an unassigned package using a delivery 
  route that's already in progress, or **Create Delivery Route**.

As a Supervisor, you have access to:
  - **View Unassigned Packages** which responds with a list of 
  unassigned packages containing their IDs and locations.

As a Manager, you can:
  - **View Active Delivery Routes** to find information about all
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