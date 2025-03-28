import csv
from pathlib import Path
from colorama import Fore
from Vehicles.truck_class_model import TruckConstants


class DistanceCalculator:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = Path(__file__).parent.parent / 'csv_file' / 'distances.csv'
        else:
            self.file_path = Path(file_path)

        self.total_distance = None
        self.distance_dict = self.load_distance_data()

    def load_distance_data(self) -> dict:
        """initializes a dictionary of distances between each city in the csv file

        Returns:
            (dict)
        """
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

    def get_distance(self, starting_point, end_point) -> int:
        """calculates distance between two cities

        Returns:
            (int)
        """
        if starting_point not in self.distance_dict or end_point not in self.distance_dict:
            raise ValueError(Fore.RED + f"City '{starting_point}' or '{end_point}' not found in the distance dictionary.")
        return self.distance_dict[starting_point][end_point]

    def calculate_total_distance(self, route) -> int:
        """calculates the total distance of the given route

        Args:
            route (list)

        Returns:
            (int)
        """
        total_distance = 0
        for i in range(len(route) - 1):
            starting_point = route[i]
            end_point = route[i + 1]
            total_distance += self.get_distance(starting_point, end_point)
        return total_distance

    def validate_route(self, route: list) -> None:
        if len(route) < 2:
            raise ValueError(Fore.RED + "Route must have at least two cities.")
        
        for city in route:
            if city not in self.distance_dict:
                raise ValueError(Fore.RED + f"City '{city}' not found in the distance dictionary.")

        for i in range(len(route) - 1):
            if route[i] == route[i + 1]:
                raise ValueError(Fore.RED + "Route can't have the same city twice in a row.")
            
        total_distance = self.calculate_total_distance(route)
        if total_distance > TruckConstants.ACTROS_MAX_RANGE:
            raise ValueError(Fore.RED + 'Total distance out of any truck max range')

    def get_route_distance(self, route_input: str) -> int:
        """takes in the entire route given as a sgtring and calculates the total distance

        Args:
            route_input (str)

        Returns:
            (int)
        """
        route = route_input.strip().split()
        self.validate_route(route)
        self.total_distance = self.calculate_total_distance(route)
        return self.total_distance

    def __str__(self) -> str:
        if self.total_distance is not None:
            return Fore.LIGHTCYAN_EX + f"Total distance calculated: {self.total_distance} km."
        return Fore.YELLOW + "No distance calculated yet."