import unittest
from colorama import Fore
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.valid_firstname = "ivan"
        self.valid_lastname = "ivan"
        self.valid_phone_number = "099999999"
        self.valid_email = "ivan@ivan"
        
        self.user = User(
            firstname=self.valid_firstname,
            lastname=self.valid_lastname,
            phone_number=self.valid_phone_number,
            email=self.valid_email
        )

    def test_initialization_withValidValues(self):
        # Check if the user is initialized correctly
        self.assertEqual(self.user.firstname, self.valid_firstname)
        self.assertEqual(self.user.lastname, self.valid_lastname)
        self.assertEqual(self.user.phone_number, self.valid_phone_number)
        self.assertEqual(self.user.email, self.valid_email)

    def test_raisesValueError_whenInvalidFirstName(self):
        # Test invalid firstname (less than 3 characters)
        with self.assertRaises(ValueError):
            User(firstname="Jo", lastname=self.valid_lastname, phone_number=self.valid_phone_number, email=self.valid_email)

    def test_raisesValueError_whenInvalidLastName(self):
        # Test invalid lastname (less than 3 characters)
        with self.assertRaises(ValueError):
            User(firstname=self.valid_firstname, lastname="Do", phone_number=self.valid_phone_number, email=self.valid_email)

    def test_raisesValueError_whenInvalidPhoneNumber(self):
        # Test invalid phone number (less than 8 characters)
        with self.assertRaises(ValueError):
            User(firstname=self.valid_firstname, lastname=self.valid_lastname, phone_number="1234567", email=self.valid_email)

    def test_raisesValueError_whenInvalidEmail(self):
        # Test invalid email (less than 6 characters or without '@')
        with self.assertRaises(ValueError):
            User(firstname=self.valid_firstname, lastname=self.valid_lastname, phone_number=self.valid_phone_number, email="short")
        with self.assertRaises(ValueError):
            User(firstname=self.valid_firstname, lastname=self.valid_lastname, phone_number=self.valid_phone_number, email="no-at-sign")

    def test_stringRepresentation(self):
        # Test string representation
        expected_str = (Fore.LIGHTCYAN_EX + f'Name: {Fore.YELLOW + self.valid_firstname} {self.valid_lastname + Fore.LIGHTCYAN_EX}\n'
                        f'Phone: {Fore.YELLOW + self.valid_phone_number + Fore.LIGHTCYAN_EX}\n'
                        f'E-mail: {Fore.YELLOW + self.valid_email + Fore.LIGHTCYAN_EX}')
        self.assertEqual(str(self.user), expected_str)