from csv_file.distance_calculator import DistanceCalculator
from colorama import Fore


class CourierCostCalculator:
    BASE_RATE = 10.0
    WEIGHT_COST_PER_KG = 2.00
    DISTANCE_COST_PER_KM = 0.075
    INSURANCE_PERCENTAGE = 5.0  

    def __init__(self, distance_calculator: DistanceCalculator) -> None:
        self._base_rate = CourierCostCalculator.BASE_RATE
        self._weight_cost_per_kg = CourierCostCalculator.WEIGHT_COST_PER_KG
        self._distance_cost_per_km = CourierCostCalculator.DISTANCE_COST_PER_KM
        self._insurance_percentage = CourierCostCalculator.INSURANCE_PERCENTAGE
        self._distance_calculator = distance_calculator

    def calculate_cost(self, package):
        start_location = package.start_location.name
        end_location = package.end_location.name
        distance = self._distance_calculator.get_distance(start_location, end_location)
        
        if distance < 0:
            raise ValueError(Fore.RED + "Distance cannot be negative.")

        initial_cost = (self._base_rate +
                        (self._weight_cost_per_kg * package.weight) +
                        (self._distance_cost_per_km * distance))
        insurance_cost = (initial_cost / 100) * self._insurance_percentage
        total_cost = initial_cost + insurance_cost

        return total_cost


# if __name__ == "__main__":
#     distance_calculator = DistanceCalculator()

#     cost_calculator = CourierCostCalculator(distance_calculator)
    
#     start_location = "SYD"  
#     end_location = "MEL"
#     contact_info = "Customer Info" 
#     package = DeliveryPackage(weight=5.0, start_location=start_location, end_location=end_location, contact_info=contact_info)

#     try:
#         total_cost = cost_calculator.calculate_cost(package)
#         print(f"The total cost for the package is: ${total_cost:.2f}")
#         print(cost_calculator) 
#     except ValueError as e:
#         print(f"An error occurred: {e}")
