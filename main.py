from delivery_package import DeliveryPackage
from locations import Locations
from user import User

alex = User('Alexander', 'Vankov', '0877455085', 'snaiper19537@gmail.com')
package = DeliveryPackage(15, Locations.SYD, Locations.BRI, alex)

print(package)
