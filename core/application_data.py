from re import escape
from models.package import Package
from models.route import Route
from models.truck import Truck, Status
from models.user import User
from models.roles import Roles

class ApplicationData:
        
    def __init__(self) -> None:
        self._packages: list[Package] = []
        self._routes: list[Route] = []
        self._trucks: list[Truck] = []
        self._users: list[User] = []
        self._logged_user = None

    @property
    def logged_in_user(self):
        if self.has_logged_in_user:
            return self._logged_user
        else:
           return f'There is no logged in user with that username!'

    @property
    def has_logged_in_user(self):
        return self._logged_user 
    
    @property
    def has_registered_users(self):
        return len(self._users) > 0

    @property
    def users(self):
        return tuple(self._users)
    @property
    def packages(self):
        return tuple(self._packages)
    
    @property
    def routes(self):
        return tuple(self._routes)
    
    @property
    def trucks(self):
        return tuple(self._trucks)

    def find_user_by_username(self, username: str) -> User:
        filtered = [user for user in self._users if user.username == username]
        if not filtered:
           raise ValueError(f"User with username {username} not found.")
        else:
            return filtered[0]

    def registrate_user(self, username, first_name, last_name, password, role, contact):
        user = User(username, first_name, last_name, password, role, contact)
        if username in self._users:
            raise ValueError(f"user with username:{username} already exists choose a different name!")
        self._users.append(user)

    def login(self, user):
        self._logged_user = user

    def logout(self):
        self._logged_user = None

    def initalize_trucks(self):
        self._trucks.extend([Truck(id,'Scania',42000,8000) for id in range(1001,1011)])
        self._trucks.extend([Truck(id,'MAN',37000,10000) for id in range(1011,1026)])
        self._trucks.extend([Truck(id,'Actros',26000,13000) for id in range(1026,1041)])

    def create_package(self, id, start_location, end_location, weight, customer_contact):
        package = Package(id, start_location, end_location, weight, customer_contact)
        self._packages.append(package)

    def create_route(self, id, locations):
            route = Route(id, locations)
            self._routes.append(route)

    def search_route(self, start_location, end_location):
        all_routes = []
        for route in self._routes:
            if start_location == route.locations[0].name and end_location == route.locations[-1].name:
                all_routes.append(route)

        if not all_routes:
            return f'No routes found for {start_location} -> {end_location}'
    
        output = ''
        for route in all_routes:
            route_output = ''
            for i, el in enumerate(route.locations):
                route_output += f'{el.name}'
                if i < len(route.locations) - 1:
                    route_output += ' -> '
            output += route_output + '\n' 

        return output.strip()  


    def update_route_assign_truck(self, route_id, truck_id):
        truck = next((t for t in self._trucks if t.id == truck_id), None)
        if not truck:
            raise ValueError(f'Truck with ID {truck_id} not found')

        if truck.is_free != Status.AVAILABLE:
            raise ValueError(f'Truck with ID {truck_id} is not available')

        route = next((r for r in self._routes if r.id == route_id), None)
        if route is None:
            raise ValueError(f'Route with ID {route_id} not found')

        route.assign_truck(truck)
        
    def update_route_assign_package(self, route_id, package_id):
        route = next((r for r in self._routes if r.id == route_id), None)
        if not route:
            raise ValueError(f'Route with ID {route_id} not found')

        package = next((p for p in self._packages if p.id == package_id), None)
        if  package is None:
            raise ValueError(f'Package with ID {package_id} not found')

        route.assign_package(package)

    def view_routes(self):
        return "\n".join(str(route) for route in self._routes)

    def view_packages(self):
        return "\n".join(str(package) for package in self._packages)

    def view_trucks(self):
        return "\n".join(str(truck) for truck in self._trucks)
    
    def get_route_by_id(self, id):
        for route in self._routes:
            if route.id == id:
                return route
            
    def get_truck_by_id(self, truck_id: int):
        for truck in self._trucks:
            if truck.id == truck_id:
                return truck

    def get_package_by_id(self, package_id: int):
        for package in self._packages:
            if package.id == package_id:
                return package
      