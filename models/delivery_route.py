from models.delivery_package import DeliveryPackage
from Vehicles.truck_class_model import TruckModel
from models.locations import Locations
from models.route_stop import RouteStop


class DeliveryRoute:
    ID = 1
    
    def __init__(self, route_id: int, departure_time: str, arrival_time: str, destinations: tuple, total_distance: int) -> None:
        self._id = route_id
        self._departure_time = departure_time
        self._arrival_time = arrival_time
        
        self._destinations: list[RouteStop] = destinations
        self._packages: list[DeliveryPackage] = list()
        self._assigned_trucks: list[TruckModel] = list()
        self._total_distance = total_distance
        
        
    def __str__(self) -> str:
        return (f'Delivery route #{self.id}\n'
                f'{self.destinations}'
                # f'{self.starting_location} - {self.final_location}\n'
                # f'Departing: {self.departure_time}'
                # f'Arriving: {self.arrival_time}'
                # f'Total distance: {self.total_distance}'
                )
        
    @property
    def id(self):
        return self._id

    ## according to distance we assign a truck
    @property
    def destinations(self):
        return tuple(self._destinations)
    
    @destinations.setter
    def destinations(self, destinations):
        self._destinations = list(destinations)
        
    @property
    def starting_location(self):
        return self._destinations[0]
    
    @property
    def final_location(self):
        return self._destinations[-1]
        
    @property
    def departure_time(self): 
        return self._destinations[0].departure_time
    
    @property
    def arrival_time(self):
        return self._destinations[-1].arrival_time
    
    @property
    def packages(self):
        return tuple(self._packages)
    
    @property
    def assigned_trucks(self):
        return tuple(self._assigned_trucks)

    @property
    def total_distance(self):
        return self._total_distance

    @classmethod
    def generate_id(cls):
        delivery_route_id = cls.ID
        cls.ID += 1
        return delivery_route_id
    
    
    def assign_package(self, package: DeliveryPackage):
        self._packages.append(package)
    
    def assign_truck(self, truck: TruckModel):
        self.truck = truck # da se proveri