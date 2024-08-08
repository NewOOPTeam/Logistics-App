from models.employee_roles import EmployeeRoles
import re

class Employee:
    id_implementer = 1

    def __init__(self, firstname: str, lastname: str, role: EmployeeRoles, username: str, password: str):
        self.firstname = firstname
        self.lastname = lastname
        self.role = role
        self.username = username
        self.password = password
        self._id = Employee.id_implementer
        Employee.id_implementer += 1

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        if len(value) < 3:
            raise ValueError('First name should be at least 3 characters long')
        if any(char.isspace() for char in value):
            raise ValueError('First name should not contain whitespace')
        self._firstname = value

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        if len(value) < 3:
            raise ValueError('Last name should be at least 3 characters long')
        if any(char.isspace() for char in value):
            raise ValueError('Last name should not contain whitespace')
        self._lastname = value

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, name):
        if len(name) < 3 or len(name) > 12:
            raise ValueError('Username should be between 3 and 12 characters long')
        if not name.isalnum():
            raise ValueError('Username should contain only letters and digits')
        if any(char.isspace() for char in name):
            raise ValueError('Username should not contain whitespace')
        self._username = name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pw):
        if len(pw) < 3 or len(pw) > 15:
            raise ValueError('Password should be between 3 and 15 characters long')
        if not re.match(r'^[a-zA-Z0-9!@#$]*$', pw):
            raise ValueError('Password should contain only letters, digits, and special symbols !@#$')
        self._password = pw
