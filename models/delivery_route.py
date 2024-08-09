from models.delivery_package import DeliveryPackage
from Vehicles.truck_class_model import TruckModel
from date_time.date_time_functionalities import DateTime
from datetime import timedelta
from models.locations import Locations
from models.route_stop import RouteStop
from csv_file.distance_calculator import DistanceCalculator as DC


class DeliveryRoute:
    ID = 1
    
    def __init__(self, route_id: int, departure_time: DateTime, arrival_time: DateTime, *destinations: Locations) -> None:
        self._id = route_id
        self._departure_time = departure_time
        self._arrival_time = departure_time + timedelta(hours = DC.calculate_total_distance(destinations) / 87)
        
        self._destinations: list[Locations] = list(destinations)
        self._packages: list[DeliveryPackage] = list()
        self._assigned_trucks: list[TruckModel] = list()

    @property
    def id(self):
        return self._id

    ## according to distance we assign a truck
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

    @classmethod
    def generate_id(cls):
        delivery_route_id = cls.ID
        cls.ID += 1
        return delivery_route_id
    
    def assign_package(self, package: DeliveryPackage):
        self._packages.append(package)
    
    def assign_truck(self, truck: TruckModel):
        self.truck = truck # da se proveri

    @property
    def departure_time(self): 
        return self._departure_time
    
    @property
    def arrival_time(self):
        return self._arrival_time
    
    

# dict with locations in the route

# total distance
# completed bool