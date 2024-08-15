from models.delivery_package import DeliveryPackage
from Vehicles.truck_class_model import TruckModel
from models.route_stop import RouteStop
from colorama import Fore

AWAITING = "Awaiting"
IN_PROGRESS = 'In progress'
COMPLETED = 'Completed'


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
        self._status = AWAITING
        
        
        
    def __str__(self) -> str:
        locations_info = [
            f"{stop.location.value} ({stop.arrival_time})"
            for stop in self._destinations
        ]
        joined_locations = '->'.join(locations_info)
        
        return (Fore.LIGHTCYAN_EX + f'Delivery route #{self.id}\n'
                f'{joined_locations}\n'
                # f'Departing: {self.departure_time}'
                # f'Arriving: {self.arrival_time}'
                f'Total distance: {self.total_distance}'
                )
        
    @property
    def id(self):
        return self._id

    @property
    def destinations(self): # this is route stops
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
    
    
    def assign_truck(self, truck: TruckModel):
        self._assigned_trucks.append(truck)
        truck.mark_unavailable()

    def complete_route(self):
        for truck in self._assigned_trucks:
            truck.mark_available()
        self._assigned_trucks.clear()

    def select_truck(self, available_trucks: list[TruckModel]):
        total_weight = self.calculate_weight_at_start()
        for truck in available_trucks:
            if truck.status == "Available" and truck.truck_capacity >= total_weight:
                self.assign_truck(truck)
                return truck
        return ValueError(Fore.RED + "No suitable truck available.") # this for create delivery

    # def calculate_total_weight(self):
    #     total_weight = 0
    #     for stop in self._destinations:
    #         for package in self._packages:
    #             if package.start_location == stop.location:
    #                 total_weight += package.weight
    #             if package.end_location == stop.location:
    #                 total_weight -= package.weight
    #     return total_weight
    
    def calculate_weight_at_each_stop(self):
        weight_at_stops = {}
        current_weight = 0
        
        for stop in self._destinations:
            for package in self._packages:
                if package.start_location == stop.location:
                    current_weight += package.weight
                if package.end_location == stop.location:
                    current_weight -= package.weight
            weight_at_stops[stop.location] = current_weight
        
        return weight_at_stops
        
    def calculate_weight_at_start(self):
        start_location = self.starting_location.location
        total_weight = sum(package.weight for package in self._packages if package.start_location == start_location)
        return total_weight

    def delivered_package(self):
        for stop in self._destinations:
            for package in self._packages:
                if package.end_location == stop.location:
                    package.status = "Completed"

    def completed_route(self,truck_id):
        for stop in self._destinations:
            if stop.location == self.final_location:
                for truck in self._assigned_trucks:
                    if truck.truck_id == truck_id:
                        truck.mark_available()
                        self._assigned_trucks.remove(truck)
        return self._assigned_trucks
    
                


        
        
        
# dict with locations in the route

# total distance
# completed bool
