from models.package import Package
from models.route import Route
from models.truck import Truck, Status

class ApplicationData:
        
    def __init__(self) -> None:
        self._packages: list[Package] = []
        self._routes: list[Route] = []
        self._trucks: list[Truck] = []

    @property
    def packages(self):
        return tuple(self._packages)
    
    @property
    def routes(self):
        return tuple(self._packages)
    
    @property
    def trucks(self):
        return tuple(self._packages)
    
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
            if start_location in route.locations and end_location in route.locations:
                start_index = route.locations.index(start_location)
                end_index = route.locations.index(end_location)
                if start_index < end_index:
                    all_routes.append(route)
        return all_routes

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

        package = next((p for p in self._packages if p.id_pack == package_id), None)
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
      