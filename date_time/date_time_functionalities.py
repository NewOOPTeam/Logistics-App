from datetime import date, timedelta, datetime


        ######## .strftime('%b %d %Y') -> displays date in format Feb 12 2024

class DateTime:
    def __init__(self) -> None:
        self.date_time = datetime
    
    @classmethod
    def create_time_stamp_for_now(self) -> str:
        """
        Creates stamp for the date and time right now
        """ #.strftime('%b %d-%Y, %I:%M')
        return datetime.now()
    
    
    def date_from_string(self, date_str: str) -> datetime:
        """
        Converts a date <str> in the format d/m/y (passed as decimals) to a <datetime> object
        """        
        format_str = '%d/%m/%y'

        try:
            return datetime.strptime(date_str, format_str)
        except ValueError:
            raise ValueError
        
    def string_from_date(self, date: datetime) -> str:    
        return date.strftime('%b %d %Y')
    
    
    def get_arrival_time_datetime(self, start_date: str, days_till_delivery: int) -> datetime:
        """
        Calculates arrival date using start date and days until delivery.
        Returns <datetime> object
        """
        start_date = self.date_from_string(start_date)
        return start_date + timedelta(days_till_delivery)

    def get_arrival_time_str(self, start_date: str, days_till_delivery: int) -> str:
        """
        Calculates arrival date using start date and days until delivery.
        Returns <str> object for printing
        """
        start_date = self.date_from_string(start_date)
        delivery_date = start_date + timedelta() # <= kilometrite/razstoianieto
        return delivery_date.strftime('%b %d %Y')
    
    
d = '12/02/24'
dt = DateTime()
d_ = dt.date_from_string(d).strftime('%b %d %Y')
arrival = dt.get_arrival_time_str('12/7/24', 3)
# arr = dt.string_from_date(arrival)

print(d_)
print(arrival, 'datetime', type(arrival))
# print(arr, 'string from date', type(arr))

