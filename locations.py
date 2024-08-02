class Locations:
    SYD = 'Sydney'
    MEL = 'Melbourne'
    ADL = 'Adelaide'
    ASP = 'Alice Springs'
    BRI = 'Brisbane'
    DAR = 'Darwin'
    PER = 'Perth'

    @classmethod
    def from_string(cls, location_string):
        if location_string not in [cls.SYD, cls.MEL, cls.ADL, cls.ASP, cls.BRI, cls.DAR, cls.PER]:
            raise ValueError(
                f'None of the possible Locations matches {location_string}.')

        return location_string

