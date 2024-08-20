import unittest
from unittest.mock import MagicMock, patch
from commands.view_all_dev_routes import ViewAllDevRoutes
from core.application_data import AppData
from models.employee_roles import EmployeeRoles
from date_time.date_time_functionalities import DateTime
from colorama import Fore
from models.delivery_package import DeliveryPackage
from Vehicles.truck_class_model import TruckModel
from models.route_stop import RouteStop
from models.delivery_route import DeliveryRoute, AWAITING, IN_PROGRESS, COMPLETED
from models.locations import Locations  

class TestViewAllDevRoutes(unittest.TestCase):
    def setUp(self):
        self.app_data = MagicMock(spec=AppData)

        self.manager_employee = MagicMock()
        self.manager_employee.role = EmployeeRoles.MANAGER
        self.app_data.logged_in_employee = self.manager_employee

        self.mock_routes = []
        for i in range(3):
            location = Locations.SYD if i == 0 else Locations.MEL

            departure_time = f'Aug 19 2024 08:{i*10:02d}h'
            arrival_time = f'Aug 19 2024 10:{i*10:02d}h'
            stop = RouteStop(location=location, departure_time=departure_time, arrival_time=arrival_time)
            
            route = DeliveryRoute(
                route_id=i+1,
                departure_time=departure_time,
                destinations=[stop],
                total_distance=10 * (i+1)
            )
            self.mock_routes.append(route)

        self.app_data.view_all_delivery_routes.return_value = '\n\n'.join(
            [f"Route: {route}\nAssigned packages: 0, total weight: 0\n" for route in self.mock_routes]
        )

    def test_initialization_successful(self):
        command = ViewAllDevRoutes([], self.app_data)
        self.assertIsInstance(command, ViewAllDevRoutes)
        self.assertEqual(command._app_data, self.app_data)

    def test_raisesValueError_whenExecuteNonManager(self):
        self.app_data.logged_in_employee.role = EmployeeRoles.EMPLOYEE

        command = ViewAllDevRoutes([], self.app_data)
        with self.assertRaises(ValueError) as context:
            command.execute()
        self.assertEqual(str(context.exception), Fore.RED + 'Only managers can view information about all delivery routes!')

    def test_executeSuccess_returnsCorrect(self):
        self.app_data.logged_in_employee.role = EmployeeRoles.MANAGER

        command = ViewAllDevRoutes([], self.app_data)

        with patch.object(DateTime, 'create_time_stamp_for_today', return_value='2024-08-19'):
            routes = command.execute()
            self.assertEqual(routes, '\n\n'.join(
                [f"Route: {route}\nAssigned packages: 0, total weight: 0\n" for route in self.mock_routes]
            ))



