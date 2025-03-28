from colorama import Fore


class User:
    def __init__(self, firstname, lastname, phone_number, email):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email

    @property
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, value) -> None:
        if len(value) < 3:
            raise ValueError()
        self._firstname = value

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, value) -> None:
        if len(value) < 3:
            raise ValueError()
        self._lastname = value

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value) -> None:
        if len(value) < 8:
            raise ValueError()
        self._phone_number = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value) -> None:
        if len(value) < 6:
            raise ValueError()
        if '@' not in value:
            raise ValueError()
        self._email = value

    def __str__(self) -> str:
        return (Fore.LIGHTCYAN_EX + f'Name: {Fore.YELLOW + self.firstname} {self.lastname + Fore.LIGHTCYAN_EX}\n'
                f'Phone: {Fore.YELLOW + self.phone_number + Fore.LIGHTCYAN_EX}\n'
                f'E-mail: {Fore.YELLOW + self.email + Fore.LIGHTCYAN_EX}')