from core.application_data import AppData
from core.command_factory import CommandFactory
from core.engine2 import Engine

app_data = AppData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()

# addcustomer Ivan Slavov 0883837373 ivan@slavov
# addpackage 34 Sydney Melbourne ivan@slavov
# viewpackage 1
# createdeliveryroute
# done