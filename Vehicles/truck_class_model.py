"""
Here will be the constants for the truck class. They will be used in the truck class to define the truck's properties.
There are constants for the truck's name, capacity, and max range.
We have 3 brands of trucks, each with a different capacity and max range.
Scania has a capacity of 42_000KG and a max range of 8_000km. We have 10 of these trucks with IDs from 1001 to 1010.
Man has a capacity of 37_000KG and a max range of 10_000km. We have 15 of these trucks with IDs from 1011 to 1025.
Actros has a capacity of 26_000KG and a max range of 13_000km. We have 15 of these trucks with IDs from 1026 to 1040.
"""
from colorama import Fore


class TruckConstants:

    SCANIA_CAPACITY = 42000
    SCANIA_MAX_RANGE = 8000
    SCANIA_TRUCKS = 10
    SCANIA_MIN_ID = 1001
    SCANIA_MAX_ID = 1010

    MAN_CAPACITY = 37000
    MAN_MAX_RANGE = 10000
    MAN_TRUCKS = 15
    MAN_MIN_ID = 1011
    MAN_MAX_ID = 1025

    ACTROS_CAPACITY = 26000
    ACTROS_MAX_RANGE = 13000
    ACTROS_TRUCKS = 15
    ACTROS_MIN_ID = 1026
    ACTROS_MAX_ID = 1040


class TruckModel:
    vehicles_id = set()

    def __init__(self, truck_id: int, truck_capacity: int, max_range: int, name: str, status='Available') -> None:
        # if truck_id in TruckModel.vehicles_id:
        #     raise ValueError(f"Truck ID {truck_id} already exists.")
        # if not self.validate_id(truck_id):
        #     raise ValueError(f"Truck ID {truck_id} is out of valid range.")
        
        self._truck_id = truck_id
        self._truck_capacity = truck_capacity
        self._max_range = max_range
        self._status = status
        self._name = name
        self._packages = []
        TruckModel.vehicles_id.add(truck_id)

    @property
    def truck_id(self):
        return self._truck_id
    
    @property
    def truck_capacity(self):
        return self._truck_capacity
    
    @truck_capacity.setter
    def truck_capacity(self, value):
        self._truck_capacity = value
    
    @property
    def max_range(self):
        return self._max_range
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if value in ['Available', 'Unavailable']:
            self._status = value
        else:
            raise ValueError(Fore.RED + "Status must be 'Available' or 'Unavailable'")
    
    @property
    def name(self):
        return self._name

    def validate_id(self, truck_id: int) -> bool:
        if TruckConstants.SCANIA_MIN_ID <= truck_id <= TruckConstants.SCANIA_MAX_ID:
            return True
        if TruckConstants.MAN_MIN_ID <= truck_id <= TruckConstants.MAN_MAX_ID:
            return True
        if TruckConstants.ACTROS_MIN_ID <= truck_id <= TruckConstants.ACTROS_MAX_ID:
            return True
        return False

    def __str__(self):
        return (Fore.LIGHTCYAN_EX + f'Truck #{self.truck_id} - {self.name}\n'
                f'Status: {self.status}\n')

