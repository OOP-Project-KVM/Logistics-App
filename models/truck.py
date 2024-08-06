# Attributes:
# id: unique identifier (int or string)
# is_free: availability status (boolean)
# name: name of the truck (string)
# capacity: maximum weight capacity in kg 
# max_range: maximum range in km



# Methods:
# __init__(self, id): constructor to initialize the attributes.
# set_availability(self, status): sets the availability status of the truck.


from status import Status


class Truck:
    def __init__(self, id: int, is_free: Status, model: str, capacity: float, max_range: float):
        self._id = id
        self._is_free = is_free
        self._model = model
        self._capacity = capacity
        self._max_range = max_range

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def is_free(self) -> Status:
        return self._is_free
    
    @is_free.setter
    def is_free(self, status):
        if status != Status.AVAILABLE or status != Status.BUSY:
            raise ValueError("Invalid status. Please use Status.AVAILABLE or Status.UNAVAILABLE.")
        else:
            self._is_free = status

    @property
    def model(self) -> str:
        return self._model
    
    @property
    def capacity(self) -> float:
        return self._capacity
    
    @property
    def max_range(self) -> float:
        return self._max_range
    
    