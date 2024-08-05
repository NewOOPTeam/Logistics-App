from Vehicles.truck_class_model import TruckModel
from Vehicles.truck_class_model import TruckConstants as tc

class TruckAutoPark:
    def __init__(self):
        self.trucks = []
        self._create_trucks()

    def _create_trucks(self):
        for truck_id in range(tc.SCANIA_MIN_ID, tc.SCANIA_MAX_ID + 1):
            self.trucks.append(TruckModel(truck_id, tc.SCANIA_CAPACITY, tc.SCANIA_MAX_RANGE, "Scania"))

        for truck_id in range(tc.MAN_MIN_ID, tc.MAN_MAX_ID + 1):
            self.trucks.append(TruckModel(truck_id, tc.MAN_CAPACITY, tc.MAN_MAX_RANGE, "Man"))

        for truck_id in range(tc.ACTROS_MIN_ID, tc.ACTROS_MAX_ID + 1):
            self.trucks.append(TruckModel(truck_id, tc.ACTROS_CAPACITY, tc.ACTROS_MAX_RANGE, "Actros"))

    def mark_unavailable(self, truck_id: int):
        truck = self.get_truck_by_id(truck_id)
        truck.status = 'Unavailable'

    def mark_available(self, truck_id: int):
        truck = self.get_truck_by_id(truck_id)
        truck.status = 'Available'

    def get_truck_by_id(self, truck_id: int) -> TruckModel:
        for truck in self.trucks:
            if truck.truck_id == truck_id:
                return truck
        raise ValueError(f'Truck ID {truck_id} does not exist.')

