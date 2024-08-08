from date_time.date_time_functionalities import DateTime
from models.locations import Locations

class RouteStop:
    def __init__(self, location: Locations, arrival_time: DateTime, departure_time: DateTime):
        self.location = location
        self.departure_time = departure_time
        self.arrival_time = arrival_time

