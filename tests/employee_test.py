import unittest
from models.employee import Employee
from models.employee_roles import EmployeeRoles

class TestEmployee(unittest.TestCase):
    def test_valid_employee(self):
        emp = Employee("John", "Doe", EmployeeRoles.ADMIN, "johndoe", "password123")
        self.assertEqual(emp.firstname, "John")
        self.assertEqual(emp.lastname, "Doe")
        self.assertEqual(emp.role, EmployeeRoles.ADMIN)
        self.assertEqual(emp.username, "johndoe")
        self.assertEqual(emp.password, "password123")

    def test_raisesValueError_whenInvalidFirstName(self):
        with self.assertRaises(ValueError):
            Employee("J", "Doe", EmployeeRoles.ADMIN, "johndoe", "password123")

    def test_raisesValueError_whenInvalidLastName(self):
        with self.assertRaises(ValueError):
            Employee("John", "D", EmployeeRoles.ADMIN, "johndoe", "password123")

    def test_raisesValueError_whenUsernameLengthIsInvalid(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", EmployeeRoles.ADMIN, "jd", "password123")

    def test_raisesValuerError_whenUsernameContainsInvalidCharacters(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", EmployeeRoles.ADMIN, "johndoe*", "password123!")

    def test_raisesValueError_whenPasswordLengthIsInvalid(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", EmployeeRoles.ADMIN, "johndoe", "pw")

    def test_raisesValuerError_whenPasswordContainsInvalidCharacters(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", EmployeeRoles.ADMIN, "johndoe", "password123*")

