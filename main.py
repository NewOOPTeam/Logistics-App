from core.application_data import AppData
from core.command_factory import CommandFactory
from core.engine import Engine


if __name__ == "__main__":
    app_data = AppData()
    cmd_factory = CommandFactory(app_data)
    engine = Engine(cmd_factory, app_data)

    engine.start()
 
# login
# logout
# help
# addcustomer
# createpackage
# viewpackage
# viewunassignedpackages
# viewallpackages
# createdeliveryroute
# viewdeliveryroute
# assigntrucktoroute
# viewalldeliveryroutes
# viewroutesinprogress
# listalltrucks
# timeforward
# done
# Aug 20 2024 17:20h

# "employee_user", "password123!",
# "supervisor_user", "password456!"
# "manager_user", "password789!"
# "admin_user", "password000!"
