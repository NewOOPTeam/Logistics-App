class User:
    def __init__(self, firstname, lastname, phone_number, email):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        if len(value) < 3:
            raise ValueError()
        self._firstname = value

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        if len(value) < 3:
            raise ValueError()
        self._lastname = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if len(value) < 8:
            raise ValueError()
        self._phone_number = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if len(value) < 6:
            raise ValueError()
        if '@' not in value:
            raise ValueError()
        self._email = value

    def __str__(self):
        return (f'Name: {self.firstname} {self.lastname}\n'
                f'Phone: {self.phone_number}\n'
                f'E-mail: {self.email}')


