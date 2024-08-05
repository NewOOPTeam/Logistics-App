class DistanceCalculator:
    def __init__(self):
        self.SYD = {'SYD': 0, 'MEL': 877, 'ADL': 1376, 'ASP': 2762, 'BRI': 909, 'DAR': 3935, 'PER': 4016}
        self.MEL = {'SYD': 877, 'MEL': 0, 'ADL': 725, 'ASP': 2255, 'BRI': 1765, 'DAR': 3752, 'PER': 3509}
        self.ADL = {'SYD': 1376, 'MEL': 725, 'ADL': 0, 'ASP': 1530, 'BRI': 1927, 'DAR': 3027, 'PER': 2785}
        self.ASP = {'SYD': 2762, 'MEL': 2255, 'ADL': 1530, 'ASP': 0, 'BRI': 2993, 'DAR': 1497, 'PER': 2481}
        self.BRI = {'SYD': 909, 'MEL': 1765, 'ADL': 1927, 'ASP': 2993, 'BRI': 0, 'DAR': 3426, 'PER': 4311}
        self.DAR = {'SYD': 3935, 'MEL': 3752, 'ADL': 3027, 'ASP': 1497, 'BRI': 3426, 'DAR': 0, 'PER': 4025}
        self.PER = {'SYD': 4016, 'MEL': 3509, 'ADL': 2785, 'ASP': 2481, 'BRI': 4311, 'DAR': 4025, 'PER': 0}
        
        self.distance_dict = {
            'SYD': self.SYD, 'MEL': self.MEL, 'ADL': self.ADL, 
            'ASP': self.ASP, 'BRI': self.BRI, 'DAR': self.DAR, 'PER': self.PER
        }

    def get_distance(self, starting_point, end_point):
        try:
            return self.distance_dict[starting_point][end_point]
        except KeyError:
            raise ValueError('City not found in the dict.')
        
    def calculate_total_distance(self, route):
        total_distance = 0
        for i in range(len(route) - 1):
            starting_point = route[i]
            end_point = route[i + 1]
            total_distance += self.get_distance(starting_point, end_point)
        return total_distance

    def route_(self, route):
        route = route.strip().split()

        if len(route) == 0:
            raise ValueError('Route is empty.')

        if len(route) == 1:
            raise ValueError('Route must have at least two cities.')

        try:
            total_distance = self.calculate_total_distance(route)
            print(f'Total distance for the route {" -> ".join(route)} is {total_distance} km')
        except ValueError as e:
            print(e)

# calculator = DistanceCalculator() - TOVA E ZA TESTVANE SAMO.

# route = "MEL SYD BRI"
# calculator.route_(route)
