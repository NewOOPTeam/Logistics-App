from models.locations import Locations
from models.user import User

UNASSIGNED = 'Unassigned'
ASSIGNED = "Assigned"
IN_PROGRESS = 'In progress'
COMPLETED = 'Completed'

class DeliveryPackage:
    id_implementer = 1
    

    def __init__(self, weight: float, start_location: Locations, end_location: Locations, contact_info: User):
        self.weight = weight
        self._start_location = start_location
        self._end_location = end_location
        self._contact_info = contact_info
        self._id = DeliveryPackage.id_implementer
        DeliveryPackage.id_implementer += 1
        self._status = UNASSIGNED
        self._assigned_route = None

    @property
    def id(self):
        return self._id

    @property
    def weight(self):
        return self._weight
    
    @property
    def start_location(self):
        return self._start_location
    
    @property
    def end_location(self):
        return self._end_location
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if value not in (UNASSIGNED, ASSIGNED, IN_PROGRESS, COMPLETED):
            raise ValueError('Invalid status!')
        self._status = value

    @weight.setter
    def weight(self, value):
        if not value > 0:
            raise ValueError()
        self._weight = value

    def __str__(self):
        return (f'#{self.id} Package ({self.weight}kg)\n'
                f'From: {self.start_location}\n'
                f'To: {self.end_location}\n'
                f'-----Client-----\n'
                f'{self._contact_info}\n'
                f'----------------\n'
                f'STATUS: {self.status}')