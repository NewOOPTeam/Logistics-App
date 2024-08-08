from models.delivery_package import DeliveryPackage
from Vehicles.truck_class_model import TruckModel
from date_time.date_time_functionalities import DateTime
from models.locations import Locations
from models.route_stop import RouteStop


class DeliveryRoute:
    ID = 0
    
    def __init__(self, route_id: int, departure_time: DateTime, arrival_time: DateTime, *destinations: RouteStop) -> None:
        self._id = route_id
        self._departure_time = departure_time
        self._arrival_time = arrival_time
        
        self._destinations: list[RouteStop] = list(destinations)
        self._packages: list[DeliveryPackage] = list()
        self._assigned_trucks: list[TruckModel] = list()

    @property
    def id(self):
        return self._id

    @classmethod
    def generate_id(cls):
        cls.ID += 1
        delivery_route_id = cls.ID
        
        return delivery_route_id
    
    @property
    def destinations(self):
        return tuple(self._destinations)
    
    @property
    def starting_location(self):
        return self.destinations[0]
    
    @property
    def final_location(self):
        return self.destinations[-1]
        
    @destinations.setter
    def destinations(self, *destinations: RouteStop):
        self._destinations = list(destinations)
        
    @property
    def packages(self):
        return tuple(self._packages)
    
    @property
    def assigned_trucks(self):
        return tuple(self._assigned_trucks)


# departure time
# arrival time
# dict with locations in the route

# total distance
# completed bool