from csv_file.distance_calculator import DistanceCalculator

calc = DistanceCalculator()

# Get route input from the user
route_input = input("Enter your route: ")

# Calculate the total distance for the route
try:
    distance = calc.get_route_distance(route_input)
    print(f'Route for package created: {route_input}, overall distance: {distance}')
except Exception as e:
    print(f"An error occurred: {e}")