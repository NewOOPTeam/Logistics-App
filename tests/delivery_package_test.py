import unittest
from models.locations import Locations
from models.user import User
from models.delivery_package import DeliveryPackage, UNASSIGNED, ASSIGNED, IN_PROGRESS, COMPLETED

class TestDeliveryPackage(unittest.TestCase):

    def setUp(self):
        self.start_location = Locations.ADL.value
        self.end_location = Locations.MEL.value
        self.contact_info = User("Ivan", "Ivan", "0888888888", "ivan@ivan")
        self.package = DeliveryPackage(10.0, self.start_location, self.end_location, self.contact_info)

    def test_id_returnsCorrect(self):
        self.assertEqual(self.package.id, 1)

    def test_weight_returnsCorrect(self):
        self.assertEqual(self.package.weight, 10.0)

    def test_startLocation_returnsCorrect(self):
        self.assertEqual(self.package.start_location, self.start_location)

    def test_endLocation_returnsCorrect(self):
        self.assertEqual(self.package.end_location, self.end_location)

    def test_status_returnsCorrect(self):
        self.assertEqual(self.package.status, UNASSIGNED)
        self.package.status = ASSIGNED
        self.assertEqual(self.package.status, ASSIGNED)
        self.package.status = IN_PROGRESS
        self.assertEqual(self.package.status, IN_PROGRESS)
        self.package.status = COMPLETED
        self.assertEqual(self.package.status, COMPLETED)

    def test_raisesValueError_whenInvalidStatus(self):
        with self.assertRaises(ValueError):
            self.package.status = "Invalid Status"

    def test_raisesValueError_whenInvalidWeight(self):
        with self.assertRaises(ValueError):
            self.package.weight = -5.0

    def test_str_returnsCorrect(self):
        expected_output = (
            f'#{self.package.id} Package ({self.package.weight}kg)\n'
            f'From: {self.package.start_location}\n'
            f'To: {self.package.end_location}\n'
            f'-----Client-----\n'
            f'{self.package._contact_info}\n'
            f'----------------\n'
            f'STATUS: {self.package.status}'
        )
        self.assertEqual(str(self.package), expected_output)
