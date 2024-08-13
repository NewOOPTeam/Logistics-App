from core.application_data import AppData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = AppData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory, app_data)

engine.start()
 
# addcustomer Ivan Slavov 0883837373 ivan@slavov
# createpackage 34 Sydney Melbourne ivan@slavov
# viewpackage 1
# createdeliveryroute BRI SYD MEL
# done

# "employee_user", "password123!",
# "supervisor_user", "password456!"

# login employee_user password123!
# Dec 12 2024 16:30h
# login supervisor_user password456! 


### validate customer number for weird characters too!!
#create delivery to check if status of paxkage is UNASSIGNED!!!