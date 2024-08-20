from models.delivery_package import DeliveryPackage, ASSIGNED_TO_TRUCK
from Vehicles.truck_class_model import TruckModel
from models.route_stop import RouteStop
from colorama import Fore
from models.locations import Locations


AWAITING = "Awaiting"
IN_PROGRESS = 'In progress'
COMPLETED = 'Completed'


class DeliveryRoute:
    ID = 1
    
    def __init__(self, route_id: int, departure_time, destinations: list[RouteStop], total_distance: int) -> None:
        self._id = route_id
        self._departure_time = departure_time
        self._destinations: list[RouteStop] = destinations
        self._packages: list[DeliveryPackage] = list()
        self._assigned_trucks: list[TruckModel] = list()
        self._total_distance = total_distance 
        self._status = AWAITING
        
    def __str__(self) -> str:
        locations_info = [
            f"{Fore.LIGHTCYAN_EX}{stop.location.value} "
            f"({Fore.YELLOW}{stop.arrival_time}{Fore.LIGHTCYAN_EX}){Fore.RESET}"
            for stop in self._destinations
        ]
        joined_locations = f'{Fore.WHITE} -> {Fore.RESET}'.join(locations_info)
        
        return (f'{Fore.CYAN}Delivery route #{self.id}\n'
                f'{joined_locations}\n'
                f'{Fore.CYAN}Total distance: {Fore.GREEN}{self.total_distance}km{Fore.RESET}\n'
                f'{Fore.CYAN}Status: {Fore.GREEN}{self._status}{Fore.RESET}'
                )
        
    @property
    def id(self) -> int:
        return self._id

    @property
    def destinations(self) -> tuple[RouteStop, ...]: 
        return tuple(self._destinations)
    
    @destinations.setter
    def destinations(self, destinations):
        self._destinations = list(destinations)
        
    @property
    def starting_location(self) -> RouteStop:
        return self._destinations[0]

    @property
    def final_location(self) -> RouteStop:
        return self._destinations[-1]
        
    @property
    def departure_time(self): 
        return self.destinations[0].departure_time
    
    @property
    def arrival_time(self):
        return self.destinations[-1].arrival_time
    
    @property
    def packages(self) -> tuple[DeliveryPackage, ...]:
        return tuple(self._packages)
    
    @property
    def assigned_trucks(self) -> tuple[TruckModel, ...]:
        return tuple(self._assigned_trucks)

    @property
    def total_distance(self) -> int:
        return self._total_distance

    @classmethod
    def generate_id(cls) -> int:
        delivery_route_id = cls.ID
        cls.ID += 1
        return delivery_route_id
    
    def assign_truck(self, truck: TruckModel) -> None:
        self._assigned_trucks.append(truck)
        truck.status = "Unavailable"

    def complete_route(self) -> bool:        
        for truck in self._assigned_trucks:
            truck.mark_available()
        self._assigned_trucks.clear()
        self._status = 'Completed'
        
    def calculate_weight_at_start(self) -> float:
        start_location = self.starting_location.location
        total_weight = sum(package.weight for package in self._packages if package.start_location == start_location)
        return total_weight
    
    def calculate_weight_at_stop(self, location: Locations) -> float:
        total_weight = 0
        for package in self._packages:
            if location == package.start_location:
                total_weight += package.weight
        
        return total_weight
                

    def delivered_package(self, date) -> None:
        for stop in self._destinations:
            for package in self._packages:
                if package.end_location == stop.location and date >= package.arrival_time and package.status == ASSIGNED_TO_TRUCK:
                    package._status = COMPLETED
    
    def all_packages_delivered(self, date) -> bool:
        self.delivered_package(date)
        if not self._packages:
            return False
        for package in self._packages:
            if package.status != COMPLETED:
                return False
        return True
    
    def update_route_status(self, date):
        if date >= self.arrival_time and self.all_packages_delivered(date) and self._status == IN_PROGRESS:
            self.complete_route()
            
    def truck_suitable_for_packages_in_route(self, truck: TruckModel) -> bool:
        truck_capacity_for_route = truck.truck_capacity
        weight_at_start = self.calculate_weight_at_start()
        if truck_capacity_for_route < weight_at_start:
            return False
        
        weight_to_pickup, weight_to_unload = {}, {}
        for stop in self.destinations:
            packages_weight_to_pickup = sum([package.weight for package in self.packages if package.start_location == stop.location])
            weight_to_pickup[stop.location] = packages_weight_to_pickup
            
            packages_weight_to_unload = sum([package.weight for package in self.packages if package.end_location == stop.location])
            weight_to_unload[stop.location] = packages_weight_to_unload
            
        truck_capacity_for_route -= weight_at_start 
        
        for stop in self.destinations:
            truck_capacity_for_route += weight_to_unload[stop.location]
            truck_capacity_for_route -= weight_to_pickup[stop.location]
        
        if truck_capacity_for_route > truck.truck_capacity:
            return False       
        
        return True