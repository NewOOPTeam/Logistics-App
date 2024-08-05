import csv
from pathlib import Path

class DistanceCalculator:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = Path(__file__).parent.parent / 'csv_file' / 'distances.csv'
        else:
            self.file_path = Path(file_path)

        self.total_distance = None
        self.distance_dict = self.load_distance_data()

    def load_distance_data(self):
        distance_dict = {}
        
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            
            header = next(reader)
            city_names = [city.strip() for city in header[1:]]
            
            for row in reader:
                city_from = row[0].strip()
                distances = list(map(int, row[1:]))
                distance_dict[city_from] = dict(zip(city_names, distances))

        return distance_dict

    def get_distance(self, starting_point, end_point):
        if starting_point or end_point not in self.distance_dict:
            raise ValueError(f"City '{starting_point}' or '{end_point}' not found in the distance dictionary.")
        return self.distance_dict[starting_point][end_point]

    def calculate_total_distance(self, route):
        total_distance = 0
        for i in range(len(route) - 1):
            starting_point = route[i]
            end_point = route[i + 1]
            total_distance += self.get_distance(starting_point, end_point)
        return total_distance

    def validate_route(self, route):
        if len(route) < 2:
            raise ValueError("Route must have at least two cities.")
        
        for city in route:
            if city not in self.distance_dict:
                raise ValueError(f"City '{city}' not found in the distance dictionary.")

        for i in range(len(route) - 1):
            if route[i] == route[i + 1]:
                raise ValueError("Route can't have the same city twice in a row.")

    def get_route_distance(self, route_input):
        route = route_input.strip().split()
        self.validate_route(route)
        self.total_distance = self.calculate_total_distance(route)
        return self.total_distance

    def __str__(self):
        if self.total_distance is not None:
            return f"Total distance calculated: {self.total_distance} km."
        return "No distance calculated yet."

# Example usage (can be removed in actual production code)
# if __name__ == "__main__":
#     calc = DistanceCalculator()  # Will use the default path
#     try:
#         route_input = input("Enter your route (e.g., 'CityA CityB CityC'): ")
#         distance = calc.get_route_distance(route_input)
#         print(f"The total distance for the route '{route_input}' is: {distance}")
#         print(calc)  # This will use the __str__ method to print total distance
#     except Exception as e:
#         print(f"An error occurred: {e}")