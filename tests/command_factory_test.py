from unittest import TestCase
from tests.constants import TestConstants as tc
from core.application_data import AppData
from core.command_factory import CommandFactory
# from commands.assign_package_to_route import AssignPackageToRoute
from commands.create_package import CreatePackage
from commands.create_delivery_route import CreateDeliveryRoute
from commands.move_time_forward import MoveTimeForward
from commands.search_delivery_route import SearchRoute
from commands.add_customer import AddCustomer
# from commands.create_delivery import CreateDelivery
from commands.view_unassigned_packages import ViewUnassignedPackages
from commands.help import Help
from commands.view_all_dev_routes import ViewAllDevRoutes
from commands.view_package import ViewPackage
from commands.view_all_packages import ViewAllPackages
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand
from commands.done import Done


class CommandShould(TestCase):
    def setUp(self) -> None:
        self.cmd_factory = CommandFactory(AppData)
        self.app_data = self.cmd_factory._app_data
        self.factory = CommandFactory(self.app_data)
    
    def test_raisesError_invalidCommandName(self):
        with self.assertRaises(ValueError):
            self.cmd_factory.create(tc.INVALID_COMMAND)
            
    def test_createLogin_createsCommand(self):
        login = self.cmd_factory.create(tc.LOGIN)
        self.assertIsInstance(login, LoginCommand)
            
    def test_createLogout_createsCommand(self):
        logout = self.cmd_factory.create(tc.LOGOUT)
        self.assertIsInstance(logout, LogoutCommand)
            
    def test_createHelp_createsCommand(self):
        help = self.cmd_factory.create(tc.HELP)
        self.assertIsInstance(help, Help)
        
    def test_createAddCustomer_createsCommand(self):
        add_customer = self.cmd_factory.create(tc.ADD_CUSTOMER)
        self.assertIsInstance(add_customer, AddCustomer)
                    
    def test_createCreatePackage_createsCommand(self):
        create_package = self.cmd_factory.create(tc.CREATE_PACKAGE)
        self.assertIsInstance(create_package, CreatePackage)
                    
    def test_createViewPackage_createsCommand(self):
        view_package = self.cmd_factory.create(tc.VIEW_PACKAGE)
        self.assertIsInstance(view_package, ViewPackage)
                    
    def test_createViewAllPackages_createsCommand(self):
        view_all_packages = self.cmd_factory.create(tc.VIEW_ALL_PACKAGES)
        self.assertIsInstance(view_all_packages, ViewAllPackages)

    def test_createCreateDeliveryRoute_createsCommand(self):
        create_delivery_route = self.cmd_factory.create(tc.CREATE_DELIVERY_ROUTE)
        self.assertIsInstance(create_delivery_route, CreateDeliveryRoute)
    
    def test_createAssignPackageToRoute_raisesErrorIncorrectParams(self):
        with self.assertRaises(ValueError):
            self.cmd_factory.create(tc.ASSIGN_PACKAGE_TO_ROUTE)
    
    def test_createViewUnassignedPackages_createsCommand(self):
        view_unass_pckgs = self.cmd_factory.create(tc.VIEW_UNASSIGNED_PACKAGES)
        self.assertIsInstance(view_unass_pckgs, ViewUnassignedPackages)
            
    def test_createViewAllDevRoutes_createsCommand(self):
        view_all_routes = self.cmd_factory.create(tc.VIEW_ALL_DELIVERY_ROUTES)
        self.assertIsInstance(view_all_routes, ViewAllDevRoutes)
            
    def test_createMoveTimeForward_createsCommand(self):
        tf = self.cmd_factory.create(tc.TIME_FORWARD)
        self.assertIsInstance(tf, MoveTimeForward)
            
    def test_createDone_createsCommand(self):
        done = self.cmd_factory.create(tc.DONE)
        self.assertIsInstance(done, Done)       