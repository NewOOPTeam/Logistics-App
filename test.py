import csv
import pathlib

class DistanceCalculator:
    def __init__(self, file_name):
        # Adjust this line to point to the correct directory
        base_directory = pathlib.Path(__file__).parent / 'data'
        self.file_path = base_directory / file_name
        print(f"Attempting to load file from: {self.file_path}")  # Debugging line
        self.distance_dict = self.load_distance_data()

    def load_distance_data(self):
        distance_dict = {}
        # Try to open the file and load data
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                
                # Read the header row to get city names for columns
                header = next(reader)
                city_names = [city.strip() for city in header[1:]]  # Extract city names from the second column onward
                
                for row in reader:
                    city_from = row[0].strip()  # Get the city name from the first column
                    try:
                        distances = list(map(int, row[1:]))  # Convert distance strings to integers
                    except ValueError:
                        raise ValueError(f"Error converting distances for city {city_from}.")
                    
                    distance_dict[city_from] = dict(zip(city_names, distances))  # Create a dictionary of distances

        except FileNotFoundError:
            raise FileNotFoundError(f"The file at {self.file_path} does not exist.")
        
        return distance_dict

    def get_distance(self, starting_point, end_point):
        try:
            return self.distance_dict[starting_point][end_point]
        except KeyError:
            raise ValueError(f"Distance between {starting_point} and {end_point} not found.")

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
                raise ValueError(f"City {city} not found in the distance dictionary.")
        
        for i in range(len(route) - 1):
            if route[i] == route[i + 1]:
                raise ValueError("Route must have different cities.")

    def get_route_distance(self, route_input):
        route = route_input.strip().split()
        self.validate_route(route)
        return self.calculate_total_distance(route)


# Example usage
file_name = 'Untitled.csv'  # Ensure this is the correct file name with extension
calculator = DistanceCalculator(file_name)

# Define the route
route_input = 'MEL ADL ASP'

# Calculate and print the distance for the route
try:
    total_distance = calculator.get_route_distance(route_input)
    print(f'Total distance for the route {" -> ".join(route_input.split())} is {total_distance} km')
except ValueError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
