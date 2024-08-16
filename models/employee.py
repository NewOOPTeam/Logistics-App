from models.employee_roles import EmployeeRoles
import re
from colorama import Fore


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
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, value) -> None:
        if len(value) < 3:
            raise ValueError(Fore.RED + 'First name should be at least 3 characters long')
        if any(char.isspace() for char in value):
            raise ValueError(Fore.RED + 'First name should not contain whitespace')
        self._firstname = value

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, value) -> None:
        if len(value) < 3:
            raise ValueError(Fore.RED + 'Last name should be at least 3 characters long')
        if any(char.isspace() for char in value):
            raise ValueError(Fore.RED + 'Last name should not contain whitespace')
        self._lastname = value

    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, name) -> None:
        if len(name) < 3 or len(name) > 20:
            raise ValueError(Fore.RED + 'Username should be between 3 and 20 characters long')
        if not re.match(r'^[a-zA-Z0-9!@#$_]*$', name):
            raise ValueError(Fore.RED + 'Username should contain only letters, digits, and special symbols !@#$_')
        if any(char.isspace() for char in name):
            raise ValueError(Fore.RED + 'Username should not contain whitespace')
        self._username = name

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, pw) -> None:
        if len(pw) < 3 or len(pw) > 20:
            raise ValueError(Fore.RED + 'Password should be between 3 and 20 characters long')
        if not re.match(r'^[a-zA-Z0-9!@#$]*$', pw):
            raise ValueError(Fore.RED + 'Password should contain only letters, digits, and special symbols !@#$')
        self._password = pw