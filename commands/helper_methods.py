class Validate:
    pass

class Parse:
    
    def to_int(val):
        pass
    
    def to_float(val):
        try:
            return float(val)
        except:
            raise ValueError('Invalid package weight')