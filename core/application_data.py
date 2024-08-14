from math import log
from re import escape
from models import user
from models.package import Package, DISTANCE_TABLE
from models.route import Route
from models.truck import Truck, Status
from models.user import User
from models.roles import Roles
import os
from datetime import datetime, timedelta,time

class ApplicationData:

    DEPARTURE_TIME = datetime.strptime("06:00", "%H:%M").time()  # Fixed departure time at 6 AM
    AVERAGE_SPEED = 87  # Average speed in km/h

    def __init__(self) -> None:
        self._packages: list[Package] = []
        self._routes: list[Route] = []
        self._trucks: list[Truck] = []
        self._users: list[User] = []
        self._logged_user = None


    def calculate_arrival_time(self, departure_time: datetime, distance: int) -> datetime:
        """
        Calculate the expected arrival time based on the distance and a fixed speed of 87 km/h.
        """
        travel_time_hours = distance / 87  # Average speed 87 km/h
        arrival_time = departure_time + timedelta(hours=travel_time_hours)
        return arrival_time


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


    def load_employees_from_file(self,file_path):
        file_path = 'models/employees.txt'
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            return []
        
        employees = []
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(' ')
                if len(data) == 6:
                    username, first_name, last_name, password, role, contact = data
                    employees.append(User(username, first_name, last_name, password, role, contact))
                    self.registrate_user(username, first_name, last_name, password, role, contact)
                else:
                    print(f'Invalid data: {line}')
        return employees
            

    def create_package(self, id, start_location, end_location, weight, customer_contact):
        package = Package(id, start_location, end_location, weight, customer_contact)
        self._packages.append(package)
        
    def create_route(self, id, locations):
            route = Route(id, locations)
            self._routes.append(route)



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

        if package is not None:
            route.assign_package(package)

    def view_routes(self):
        output = []
        for route in self._routes:
            output.append(f"\nId: {route.id}")
            output.append(f"Locations: {[loc.name for loc in route.locations]}")
            output.append(f"Truck: {route.truck.model if route.truck else 'None'}")
            output.append(f"Weight: {sum(pkg.weight for pkg in route.packages):.2f}")
            output.append(f"Distance: {self.calculate_total_distance(route)}")
            output.append(f"Departure time: {route.departure_time.strftime('%H:%M:%S') if route.departure_time else 'Not set'}")
        
            if route.packages:
                for pkg in route.packages:
                    eta = pkg.expected_arrival_time.strftime('%b %dth %H:%M') if pkg.expected_arrival_time else 'Not available'
                    output.append(f"Package ID: {pkg.id}, ETA: {eta}")
            else:
                output.append("No packages assigned to this route.")

        return "\n".join(output)
    
    def calculate_total_distance(self, route):
        """
        Calculate the total distance of a route by summing the distances between consecutive locations.
        """
        locations = route.locations
        total_distance = 0
        for i in range(len(route.locations) - 1):
            start_location = locations[i].name
            end_location = locations[i + 1].name
            distance = DISTANCE_TABLE[start_location][end_location]
            total_distance += distance
        return total_distance


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

    def get_package_by_id(self, package_id: str):
        for package in self._packages:
            if package.id == package_id:
                return package
        return None
    
    
    def assign_package_to_route(self, package_id: str, route_id: str, departure_date: datetime):
        package = self.get_package_by_id(package_id)
        route = self.get_route_by_id(route_id)

        if package is None:
            raise ValueError(f"Package with ID {package_id} not found.")
    
        if route is None:
            raise ValueError(f"Route with ID {route_id} not found.")
    
        if not route.truck:
            raise ValueError("Cannot assign package to a route with no truck assigned.")

        route_departure_time = datetime.combine(departure_date, time(6, 0))
        route.departure_time = route_departure_time

        start_location = route.locations[0].name
        destination = package.end_location
        total_distance = DISTANCE_TABLE[start_location][destination]

        # Calculate the arrival time based on the fixed departure time and distance
        arrival_time = self.calculate_arrival_time(route_departure_time, total_distance)

        # Assign the package to the route and set its expected arrival time
        route.assign_package(package)
        package.expected_arrival_time = arrival_time

        print(f"Package {package.id} assigned to Route {route.id} with expected arrival at {arrival_time}")


    def search_route(self, start_location: str, end_location: str):
        """
        Search for routes that go from start_location to end_location and display them with full timing details.
        """
        start_location = start_location.upper()
        end_location = end_location.upper()
    
        matching_routes = []
    
        for route in self._routes:
            location_names = [loc.name for loc in route.locations]
            if start_location in location_names and end_location in location_names:
                start_index = location_names.index(start_location)
                end_index = location_names.index(end_location)
            
                if start_index < end_index:
                    matching_routes.append(route)

        if matching_routes:
            for route in matching_routes:
                start_index = [loc.name for loc in route.locations].index(start_location)
                end_index = [loc.name for loc in route.locations].index(end_location)
            
                print(f"\nRoute {route.id}:")
                loc_time = route.departure_time
                for i in range(start_index, end_index + 1):
                    loc_name = route.locations[i].name
                   
                    
                    if i > start_index:  # Skip this for the first location since it's the departure point
                        prev_loc_name = route.locations[i - 1].name
                        distance = DISTANCE_TABLE[prev_loc_name][loc_name]
                        loc_time += timedelta(hours=distance / 87)  # Add travel time based on distance and speed
                
                    formatted_time = loc_time.strftime('%b %dth %H:%M')
                
                    if i < end_index:
                        print(f"{loc_name} ({formatted_time}) → ", end="")
                    else:
                        print(f"{loc_name} ({formatted_time})")
        else:
            print(f"No routes found from {start_location} to {end_location}.")