# from delivery_package import DeliveryPackage
# from locations import Locations
# from user import User

# alex = User('Alexander', 'Vankov', '0877455085', 'snaiper19537@gmail.com')
# package = DeliveryPackage(15, Locations.SYD, Locations.BRI, alex)

# print(package)

from core.application_data import AppData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = AppData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()