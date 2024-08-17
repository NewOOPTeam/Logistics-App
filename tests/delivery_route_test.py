import unittest
from colorama import Fore
from Vehicles.truck_class_model import TruckModel
from models.delivery_package import DeliveryPackage
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
    
    def test_str_returnsCorrectString(self):
        expected_str = (
            Fore.LIGHTCYAN_EX + 
            'Delivery route #1\n' +
            'Sydney (Dec 12 2024 16:30h) -> Melbourne (Dec 12 2024 20:30h)\n' +
            'Total distance: 877km'
        )
        self.assertEqual(str(self.delivery_route), expected_str)

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

    def test_calculateWeightAtEachStop_returnsCorrectWeights(self):
        package1 = DeliveryPackage(200, self.destinations[0].location, self.destinations[1].location, contact_info='John Doe')
        package2 = DeliveryPackage(300, self.destinations[0].location, self.destinations[1].location, contact_info='Jane Doe')
        self.delivery_route._packages.extend([package1, package2])
        weight_at_stops = self.delivery_route.calculate_weight_at_each_stop()
        self.assertEqual(weight_at_stops[self.destinations[0].location], 500)
        self.assertEqual(weight_at_stops[self.destinations[1].location], 0)

    def test_deliveredPackage_marksPackagesAsCompleted(self):
        package1 = DeliveryPackage(200, self.destinations[0].location, self.destinations[1].location, contact_info='John Doe')
        package2 = DeliveryPackage(300, self.destinations[0].location, self.destinations[1].location, contact_info='Jane Doe')
        self.delivery_route._packages.extend([package1, package2])
        self.delivery_route.delivered_package()
        self.assertEqual(package1.status, "Completed")
        self.assertEqual(package2.status, "Completed")