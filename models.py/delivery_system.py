# Attributes:
# packages: list of all Package objects
# routes: list of all Route objects
# trucks: list of all Truck objects


# Methods:
# __init__(self): constructor to initialize the attributes.
# create_package(self, id, start_location, end_location, weight, customer_contact): creates a new package and adds it to the list.
# create_route(self, id, locations): creates a new route and adds it to the list.
# search_route(self, start_location, end_location): searches for routes based on the package's start and end locations.
# update_route_assign_truck(self, route_id, truck_id): assigns a free truck to a route.
# update_route_assign_package(self, route_id, package_id): assigns a delivery package to a route.
# view_routes(self): displays information about all routes.
# view_packages(self): displays information about all packages.
# view_trucks(self): displays information about all trucks.


## TODO MYKYTA