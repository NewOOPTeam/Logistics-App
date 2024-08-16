from models.locations import Locations
from colorama import Fore


class RouteStop:
    def __init__(self, location: Locations, arrival_time: str, departure_time: str):
        self._location = location
        self._departure_time = departure_time
        self._arrival_time = arrival_time

    def __str__(self) -> str:
        return (Fore.LIGHTCYAN_EX + f'Location: {self._location}\n'
                f'Departure Time: {self._departure_time}'
                f'Arrival Time: {self._arrival_time}\n')

    @property
    def location(self) -> Locations:
        return self._location

    @property
    def departure_time(self):
        return self._departure_time

    @property
    def arrival_time(self):
        return self._arrival_time