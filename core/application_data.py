
from models.package import Package, DISTANCE_TABLE
from models.route import Route
from models.truck import Truck, Status
from models.user import User
from models.roles import Roles
import os
from datetime import datetime, timedelta
from models.route_status import RouteStatus
from models.package_status import PackageStatus

class ApplicationData:
    AVERAGE_SPEED = 87  # Average speed in km/h

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
        self._trucks.extend([Truck(id, 'Scania', 42000, 8000) for id in range(1001, 1011)])
        self._trucks.extend([Truck(id, 'MAN', 37000, 10000) for id in range(1011, 1026)])
        self._trucks.extend([Truck(id, 'Actros', 26000, 13000) for id in range(1026, 1041)])

    def load_employees_from_file(self, file_path):
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

    def create_route(self, id, locations, departure_time: datetime):
        route = Route(id, locations)
        route.departure_time = departure_time
        route.status = RouteStatus.PENDING
        self._routes.append(route)
        

    def get_routes_inProgress(self):
        in_progress_routes = [route for route in self._routes if route.status == RouteStatus.INPROGRESS]
        return in_progress_routes

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

    def check_in_progress_routes(self):
        for route in self._routes:
            if route.departure_time and route.departure_time <= datetime.now() and route.status == RouteStatus.PENDING:
                route.status = RouteStatus.INPROGRESS


    def update_route_assign_package(self, route_id, package_id):
        route = next((r for r in self._routes if r.id == route_id), None)
        if not route:
            raise ValueError(f'Route with ID {route_id} not found')

        package = next((p for p in self._packages if p.id == package_id), None)
        if package is None:
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
            output.append(f"Distance: {self.calculate_total_distance(route)}km")
            output.append(f'eta:{route.arrival_time}')
            output.append(
                f"Departure time: {route.departure_time.strftime('%H:%M:%S') if route.departure_time else 'Not set'}")
            output.append(f'Status: {route.status.value}')

            if route.current_location:
                idx = route.locations.index(route.current_location)
                if len(route.locations) <= idx:
                    output.append("Next stop: We are at the last stop")

                next_location = route.locations[idx + 1].name
                output.append(f"Next Stop: {next_location}")

            if route.packages:
                for pkg in route.packages:
                    if isinstance(pkg.expected_arrival_time, str):
                        pkg.expected_arrival_time = datetime.fromisoformat(pkg.expected_arrival_time)

                    eta = pkg.expected_arrival_time.strftime(
                        '%b %dth %H:%M') if pkg.expected_arrival_time is not None else 'Not available'
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
            start_location = locations[i].name.upper()
            end_location = locations[i + 1].name.upper()
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

                    if loc_name == end_location:
                        eta_for_city = loc_time  # Save the ETA for the destination city

                    if i < end_index:
                        print(f"{loc_name} ({formatted_time}) → ", end="")
                    else:
                        print(f"{loc_name} ({formatted_time})")
        else:
            print(f"No routes found from {start_location} to {end_location}.")
        return ''

    def calculate_eta_for_route(self, route: Route, destination: str):
        """
        Calculate the ETA for a specific destination on a given route.
        """
        destination = destination.upper()

        loc_time = route.departure_time

        if loc_time is None:
            raise ValueError("Departure time for the route is not set.")

        location_names = [loc.name for loc in route.locations]

        if destination in location_names:
            start_index = 0  # The route starts from the first location.
            end_index = location_names.index(destination)

            for i in range(start_index, end_index + 1):
                loc_name = route.locations[i].name

                if i > start_index:  # Skip this for the first location since it's the departure point.
                    prev_loc_name = route.locations[i - 1].name
                    distance = DISTANCE_TABLE[prev_loc_name][loc_name]
                    loc_time += timedelta(hours=distance / 87)  # Add travel time based on distance and speed.

                if loc_name == destination:
                    Route.arrival_time = loc_time
                    return loc_time  # Return the ETA for the destination.

        return None  # Return None if the destination is not on the route.


    # def check_and_unload_packages(self, route: Route):
    #     """
    #     Check if the route has reached the current location and unload packages if the ETA has passed.
    #     Also, update the route status and truck availability.
    #     """
    #     if route.current_location is None or route.departure_time is None:
    #         return "Current location or departure time not set."
        
    #     loc_time = route.departure_time
    #     current_time = datetime.now()

    #     delivered_packages = []
    #     current_time = datetime.now().strftime('%H:%M')

    #     for i in range(len(route._locations)):
    #         loc_name = route._locations[i].name
    #         if i > 0:
    #             prev_loc_name = route._locations[i - 1].name
    #             distance = DISTANCE_TABLE[prev_loc_name][loc_name]
    #             loc_time += timedelta(hours=distance / 87)
    #         if current_time >= loc_time.strftime('%H:%M'):
    #             route._current_location = loc_name #type: ignore
    #             break


    #     # Check if the current time is past the ETA
    #         if current_time >= route._arrival_time.strftime('%H:%M') : #type: ignore
    #             route.status = RouteStatus.COMPLETED
    #             if route.truck:
    #                 route.truck.is_free = Status.AVAILABLE  # Mark the truck as available
    #                 route.truck = None  # type: ignore

        
    #         for package in route.packages:
    #             if loc_name == package.end_location:  # Assuming the last location is the destination
    #                 package.pack_status = PackageStatus.DELIVERED
    #                 delivered_packages.append(package)

    #         # Remove delivered packages from the route
    #         for package in delivered_packages:
    #             route.packages.remove(package)
    #             route._current_load -= package.weight

    #         if delivered_packages:
    #             return f"Delivered packages at {route.locations[-1].name}: {[package.id for package in delivered_packages]}"
    #         else:
    #             return f"No packages delivered at {route.locations[-1].name}."

    # def check_and_unload_packages(self, route: Route):
    #     """
    #     Check if the route has reached the current location based on the elapsed time since departure,
    #     unload packages if the ETA has passed, and update the route status and truck availability.
    #     """
    #     if route.current_location is None or route.departure_time is None:
    #         return "Current location or departure time not set."
        
    #     loc_time = route.departure_time
    #     current_time = datetime.now()

    #     for i in range(len(route._locations)):
    #         loc_name = route._locations[i].name
            
    #         if i > 0:
    #             prev_loc_name = route._locations[i - 1].name
    #             distance = DISTANCE_TABLE[prev_loc_name][loc_name]
    #             loc_time += timedelta(hours=distance / ApplicationData.AVERAGE_SPEED)
            
    #         if current_time >= loc_time:
    #             route._current_location = loc_name #type: ignore
            
    #         # Unload packages at the current location
    #         delivered_packages = []
    #         for package in route.packages:
    #             if route._current_location == package.end_location:
    #                 package.pack_status = PackageStatus.DELIVERED
    #                 delivered_packages.append(package)
            
    #         # Remove delivered packages from the route
    #         for package in delivered_packages:
    #             route.packages.remove(package)
    #             route._current_load -= package.weight

    #         if delivered_packages:
    #             print(f"Delivered packages at {route._current_location}: {[package.id for package in delivered_packages]}")

    #         # Check if the route has reached its final destination
    #         if route._current_location == route._locations[-1].name:
    #             route.status = RouteStatus.COMPLETED
    #             if route.truck:
    #                 route.truck.is_free = Status.AVAILABLE  # Mark the truck as available
    #                 route.truck = None  #type: ignore
    #             return f"Route completed. Delivered packages at {route._current_location}: {[package.id for package in delivered_packages]}"

    #     return f"Route {route.id} is in progress. Current location: {route._current_location}"

