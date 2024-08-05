class EmployeeRoles:
    ADMIN = "Admin"
    SUPERVISOR = "Supervisor"
    EMPLOYEE = "Employee"

    @classmethod
    def from_string(cls, role_string):
        if role_string not in [cls.ADMIN, cls.SUPERVISOR, cls.EMPLOYEE]:
            raise ValueError(
                f'None of the possible Roles matches {role_string}.')

        return role_string
