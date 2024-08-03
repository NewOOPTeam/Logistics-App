from locations import Locations
from user import User


class DeliveryPackage:
    packages_ids = []
    id_implementer = 1

    def __init__(self, weight: float, start_location: Locations, end_location: Locations, contact_info: User):
        self._id = DeliveryPackage.id_implementer
        DeliveryPackage.packages_ids.append(self._id)
        self._weight = weight
        self._start_location = start_location
        self._end_location = end_location
        self._contact_info = contact_info
        DeliveryPackage.id_implementer += 1

    @property
    def id(self):
        return self._id

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if not value > 0:
            raise ValueError()
        self._weight = value

    def __str__(self):
        return (f'#{self.id} Package ({self.weight}kg)\n'
                f'From: {self._start_location}\n'
                f'To: {self._end_location}\n'
                f'-----Client-----\n'
                f'{self._contact_info}\n'
                f'----------------')





