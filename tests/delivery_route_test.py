import re
import unittest
from unittest.mock import Mock
from colorama import Fore
from Vehicles.truck_class_model import TruckModel
from models.delivery_package import ASSIGNED_TO_TRUCK, DeliveryPackage
from models.delivery_route import DeliveryRoute
from models.route_stop import RouteStop
from models.locations import Locations

AWAITING = "Awaiting"
IN_PROGRESS = 'In progress'
COMPLETED = 'Completed'

class TestDeliveryRoute(unittest.TestCase):

    def setUp(self):
        self.route_id = 1
        self.departure_time = "Dec 12 2024 16:30h"
        
        location_syd = Locations(Locations.SYD)
        location_mel = Locations(Locations.MEL)
        self.destinations = [
            RouteStop(location_syd, "Dec 12 2024 16:30h", "16:30h"),
            RouteStop(location_mel, "Dec 12 2024 20:30h", "20:00h")
        ]
        self.total_distance = 877
        self.delivery_route = DeliveryRoute(self.route_id, self.departure_time, self.destinations, self.total_distance)

    def test_routeID_returnsCorrectID(self):
        self.assertEqual(self.route_id, self.delivery_route.id)

    def test_destinations_returnsCorrectDestinations(self):
        self.assertEqual(self.delivery_route.destinations, tuple(self.destinations))
    
    def test_totalDistance_returnsCorrectDistance(self):
        self.assertEqual(self.total_distance, self.delivery_route.total_distance)
    
    @staticmethod
    def remove_ansi_escape_codes(text):
        ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', text)

    def test_str_returnsCorrectString(self):
        stop1 = RouteStop(location=Mock(value="Sydney"), arrival_time="Dec 12 2024 16:30h", departure_time="Dec 12 2024 16:30h")
        stop2 = RouteStop(location=Mock(value="Melbourne"), arrival_time="Dec 12 2024 20:30h", departure_time="Dec 12 2024 20:00h")
        
        delivery_route = DeliveryRoute(
            route_id=self.route_id,
            departure_time=self.departure_time,
            destinations=[stop1, stop2],
            total_distance=self.total_distance
        )
        delivery_route._status = AWAITING 
        
        locations_info = [
            f"{Fore.LIGHTCYAN_EX}{stop.location.value} ({Fore.YELLOW}{stop.arrival_time}{Fore.LIGHTCYAN_EX}){Fore.RESET}"
            for stop in delivery_route.destinations
        ]
        joined_locations = f'{Fore.WHITE} -> {Fore.RESET}'.join(locations_info)
        
        expected_str = (
            f'{Fore.CYAN}Delivery route #{delivery_route.id}{Fore.RESET}\n'
            f'{joined_locations}\n'
            f'{Fore.CYAN}Total distance: {Fore.GREEN}{delivery_route.total_distance}km{Fore.RESET}\n'
            f'{Fore.CYAN}Status: {Fore.GREEN}{delivery_route._status}{Fore.RESET}'
        )
        
        actual_str = str(delivery_route)

        self.assertEqual(self.remove_ansi_escape_codes(actual_str), self.remove_ansi_escape_codes(expected_str))

    def test_startingLocation_returnsCorrectStartingLocation(self):
        self.assertEqual(self.destinations[0], self.delivery_route.starting_location)

    def test_finalLocation_returnsCorrectFinalLocation(self):
        self.assertEqual(self.destinations[-1], self.delivery_route.final_location)

    def test_departureTime_returnsCorrectDepartureTime(self):
        self.assertEqual(self.destinations[0].departure_time, self.delivery_route.departure_time)

    def test_arrivalTime_returnsCorrectArrivalTime(self):
        self.assertEqual(self.destinations[-1].arrival_time, self.delivery_route.arrival_time)

    def test_packages_returnsEmptyTuple(self):
        self.assertEqual(self.delivery_route.packages, tuple())

    def test_assignedTrucks_returnsEmptyTuple(self):
        self.assertEqual(self.delivery_route.assigned_trucks, tuple())

    def test_generateID_returnsCorrectID(self):
        self.assertEqual(DeliveryRoute.ID, DeliveryRoute.generate_id())

    def test_assignTruck_addsTruckToAssignedTrucks(self):
        truck = TruckModel(truck_id=1, truck_capacity=42000, max_range=8000, name='Scania', status="Available")
        self.delivery_route.assign_truck(truck)
        self.assertEqual(len(self.delivery_route.assigned_trucks), 1)
        self.assertEqual(self.delivery_route.assigned_trucks[0], truck)
        self.assertEqual(truck.status, "Unavailable")

    def test_completeRoute_marksTrucksAsAvailableAndClearsAssignedTrucks(self):
        truck = TruckModel(truck_id=1, truck_capacity=42000, max_range=8000, name='Scania', status="Unavailable")
        self.delivery_route.assign_truck(truck)
        self.delivery_route.complete_route()
        self.assertEqual(len(self.delivery_route.assigned_trucks), 0)
        self.assertEqual(truck.status, "Available")

    def test_calculateWeightAtStart_returnsCorrectWeight(self):
        package1 = DeliveryPackage(weight=100, start_location=Locations.SYD, end_location=Locations.MEL, contact_info="Ivan Ivan")
        package2 = DeliveryPackage(weight=200, start_location=Locations.SYD, end_location=Locations.MEL, contact_info="Toni Toni")
        
        package1.status = ASSIGNED_TO_TRUCK
        package2.status = ASSIGNED_TO_TRUCK
        
        self.delivery_route._packages.extend([package1, package2])
        
        self.assertEqual(self.delivery_route.calculate_weight_at_start(), 300)

   