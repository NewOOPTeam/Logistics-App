from models.employee_roles import EmployeeRoles


class Employee:
    id_implementer = 1

    def __init__(self, firstname, lastname, role: EmployeeRoles):
        self.firstname = firstname
        self.lastname = lastname
        self.role = role
        self._id = Employee.id_implementer
        Employee.id_implementer += 1

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        if len(value) < 3:
            raise ValueError
        self._firstname = value

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        if len(value) < 3:
            raise ValueError
        self._lastname = value