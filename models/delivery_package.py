from models.locations import Locations
from models.user import User
from colorama import Fore
from models.courier_cost_calculator import CourierCostCalculator
from csv_file.distance_calculator import DistanceCalculator


UNASSIGNED = 'Unassigned'
ASSIGNED_TO_TRUCK = "Assigned to truck"
ASSIGNED_TO_ROUTE = "Assigned to route"
IN_PROGRESS = 'In progress'
COMPLETED = 'Completed'


class DeliveryPackage:
    id_implementer = 1

    def __init__(self, weight: float, start_location: Locations, end_location: Locations, contact_info: User):
        self._weight = weight
        self._start_location = start_location
        self._end_location = end_location
        self._contact_info = contact_info
        self._id = DeliveryPackage.id_implementer
        DeliveryPackage.id_implementer += 1
        self._status = UNASSIGNED
        self._assigned_route = None
        self._total_cost = self.total_cost()

    @property
    def id(self) -> int:
        return self._id

    @property
    def weight(self) -> float:
        return self._weight
    
    @property
    def start_location(self) -> Locations:
        return self._start_location
    
    @property
    def end_location(self) -> Locations:
        return self._end_location
    
    @property
    def status(self) -> str:
        return self._status
    
    @status.setter
    def status(self, value) -> None:
        if value not in (UNASSIGNED, ASSIGNED_TO_TRUCK, ASSIGNED_TO_ROUTE, IN_PROGRESS, COMPLETED):
            raise ValueError(Fore.RED + 'Invalid status!')
        self._status = value

    @weight.setter
    def weight(self, value) -> None:
        if value <= 0:
            raise ValueError(Fore.RED + 'Weight must be positive.')
        self._weight = value
        
    @property    
    def arrival_time(self):
        if self._assigned_route is None:
            return 'Package awaiting assignment to route'
        for destination in self._assigned_route.destinations:
            if destination.location == self.end_location:
                return destination.arrival_time

    def __str__(self) -> str:
        return (Fore.LIGHTCYAN_EX + f'#{self.id} Package ' + Fore.YELLOW + f'{self.weight:.2f}kg' + Fore.LIGHTCYAN_EX + '\n'
                f'From: {Fore.YELLOW + self.start_location.value + Fore.LIGHTCYAN_EX}\n'
                f'To: {Fore.YELLOW + self.end_location.value + Fore.LIGHTCYAN_EX}\n'
                f'-----Client-----\n'
                f'{self._contact_info}\n'
                f'----------------\n'
                f'STATUS: {self.status}\n'
                f'Expected delivery: {Fore.YELLOW + self.arrival_time + Fore.LIGHTCYAN_EX}\n'
                f'Suggested cost: {self._total_cost:.2f}AUSD'
                )
        
    def update_status(self, date):
        if date >= self.arrival_time and self.status == ASSIGNED_TO_TRUCK:
            self.status = COMPLETED
            
    def total_cost(self):
        calculator = CourierCostCalculator(DistanceCalculator())
        total_cost = calculator.calculate_cost(self)
        
        return total_cost
