from models.delivery_package import DeliveryPackage
from Vehicles.truck_class_model import TruckModel
from date_time.date_time_functionalities import DateTime


class DeliveryRoute:
    ID = 1
    
    def __init__(self, route_id: int, departure_time: str) -> None:
        self._id = route_id
        self._departure_time = departure_time
        self._packages: list[DeliveryPackage] = list()
        self._assigned_trucks: list[TruckModel] = list()

    @property
    def id(self):
        return self._id

    @classmethod
    def generate_id(self):
        DeliveryRoute.ID += 1
        delivery_route_id = DeliveryRoute.ID
        
        return delivery_route_id
    
    
    
    
    
    
    # id
    # list of packages
    # init: assigned truck
    # departure time
    # arrival time
    # dict with locations in the route


# date time module
# total distance
# completed bool