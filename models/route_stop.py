from models.locations import Locations

class RouteStop:
    def __init__(self, location: Locations, arrival_time: str, departure_time: str):
        self.location = location
        self.departure_time = departure_time
        self.arrival_time = arrival_time

