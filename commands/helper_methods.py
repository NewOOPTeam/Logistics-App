
class Validate:
    
    @staticmethod
    def str_len(val, min, max):
        if not min <= len(val) <= max:
            raise ValueError(f'Invalid input')



class Parse:
    
    @staticmethod
    def to_int(val):
        try:
            return int(val)
        except:
            raise ValueError()
    
    @staticmethod
    def to_float(val):
        try:
            return float(val)
        except:
            raise ValueError('Invalid package weight')