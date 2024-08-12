import unittest
from models.employee import Employee
from models.employee_roles import EmployeeRoles

<<<<<<< HEAD
=======

>>>>>>> origin/main
class TestEmployee(unittest.TestCase):
    def test_valid_employee(self):
        emp = Employee("John", "Doe", EmployeeRoles.ADMIN, "johndoe", "password123")
        self.assertEqual(emp.firstname, "John")
        self.assertEqual(emp.lastname, "Doe")
        self.assertEqual(emp.role, EmployeeRoles.ADMIN)
        self.assertEqual(emp.username, "johndoe")
        self.assertEqual(emp.password, "password123")

    def test_invalid_firstname(self):
        with self.assertRaises(ValueError):
            Employee("J", "Doe", EmployeeRoles.ADMIN, "johndoe", "password123")

    def test_invalid_lastname(self):
        with self.assertRaises(ValueError):
            Employee("John", "D", EmployeeRoles.ADMIN, "johndoe", "password123")

    def test_invalid_username_length(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", EmployeeRoles.ADMIN, "jd", "password123")

    def test_invalid_username_characters(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", EmployeeRoles.ADMIN, "johndoe*", "password123!")

    def test_invalid_password_length(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", EmployeeRoles.ADMIN, "johndoe", "pw")

    def test_invalid_password_characters(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", EmployeeRoles.ADMIN, "johndoe", "password123*")

<<<<<<< HEAD
if __name__ == '__main__':
    unittest.main()
=======

if __name__ == '__main__':
    unittest.main()
>>>>>>> origin/main
