from datetime import timedelta, datetime

        ######## .strftime('%b %d %Y') -> displays date in format Feb 12 2024
class DateTime:


    @staticmethod
    def create_time_stamp_for_today() -> str:
        """
        Creates stamp for the date and time right now
        """
        return datetime.now().strftime('%b %d %Y %H:%Mh')
    
    @staticmethod
    def date_from_string(date_str: str) -> datetime:
        """
        Converts a date <str> in the format d/m/y (passed as decimals) to a <datetime> object
        """     
        format_str = '%b %d %Y %H:%Mh'
        date = datetime.strptime(date_str, format_str)  
        return date

            
    @staticmethod    
    def string_from_date(date: datetime) -> str:    
        return date.strftime('%b %d %Y %H:%Mh') 
    
    @staticmethod
    def get_arrival_time_datetime(start_date: str, days_till_delivery: int) -> datetime:
        """
        Calculates arrival date using start date and days until delivery.
        Returns <datetime> object
        """
        start_date = DateTime.date_from_string(start_date)
        return start_date + timedelta(days_till_delivery)

    @staticmethod
    def get_arrival_time_str(start_date: str, distance: int) -> str:
        """
        Calculates arrival date using start date and days until delivery.
        Returns <str> object for printing
        """
        start_date = DateTime.date_from_string(start_date)
        delivery_date = start_date + timedelta(hours= (distance // 87) + 4, minutes= distance % 87) 
        return delivery_date.strftime('%b %d %Y %H:%Mh')
    
    @staticmethod
    def future_date():
        """
        Sets the date to five days in the future
        """
        now = datetime.now()
        future_date = now + timedelta(days=5)

        return future_date.strftime('%b %d %Y %H:%Mh')


# start_date = '12/07/24 06:00'
# distance = 909
# arrival = DateTime.get_arrival_time_str(start_date, distance)
# print(arrival)
# print(type(arrival))