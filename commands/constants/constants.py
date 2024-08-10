CANCEL = 'cancel'
OPERATION_CANCELLED = 'Operation cancelled, returning to main menu'

WELCOMING_MESSAGE = """
╔══════════════════════════════════╗
║     WELCOME TO ROUTE MASTER      ║
║                                  ║
║      Plan. Track. Deliver.       ║
║                                  ║
║    Type 'help' to get started!   ║
╚══════════════════════════════════╝
"""

DESCRIPTION_MESSAGE = """
====================================================================
You need to LOGIN as either ADMIN, MANAGER, SUPERVISOR or EMPLOYEE
====================================================================

As an Employee, you are able to:
  - CREATEPACKAGE for an existing customer or add a new customer to 
    the database. You will be able to assign it for delivery right 
    away, or withhold delivery for now, if no trucks are available.
  - VIEWPACKAGE upon request to check its status, assigned route, 
    and customer linked to it.
  - CREATEDELIVERY for an unassigned package using a delivery route 
    that's already in progress, or CREATEDELIVERYROUTE.

As Supervisor, you have access to:
  - VIEWUNASSIGNEDPACKAGES which responds with a list of unassigned 
    packages containing their IDs and locations.

The Manager is able to:
  - VIEWACTIVEDELIVERYROUTES to find information about all delivery 
    routes in progress. The system responds showing each route's 
    stops, delivery weight, and the expected current stop based on 
    the time of day.
====================================================================
"""

LOGIN_MESSAGE = 'Please login in order to use the system'