from typing import List
from location import Location
from truck import Truck
from package import Package

# Attributes:
# id: unique identifier (int or string)
# locations: list of Location objects
# truck: assigned truck (Truck object or None)
# packages: list of Package objects assigned to the route


# Methods:
# __init__(self, id, locations): constructor to initialize the attributes.
# assign_truck(self, truck): assigns a free truck to the route.
# assign_package(self, package): assigns a delivery package to the route.




class Route:
    def __init__(self, id: int, locations: List[Location]):
        self._id = id
        self._locations = locations
        self._truck = None
        self._packages = []

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def locations(self) -> List[Location]:
        return self._locations
    
    @locations.setter
    def locations(self, locations: List[Location]):
        self._locations = locations

    @property
    def truck(self) -> Truck:
        return self._truck
    
    @truck.setter
    def truck(self, truck: Truck):
        self._truck = truck

    @property
    def packages(self) -> List[Package]:
        return self._packages
    
    @packages.setter
    def packages(self, packages: List[Package]):
        self._packages = packages

    def assign_truck(self, truck: Truck):
        self._truck = truck

    def assign_package(self, package: Package):
        self._packages.append(package)

    def assign_package(self, package):
        self.packages.append(package)