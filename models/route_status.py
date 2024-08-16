from enum import Enum


class RouteStatus(Enum):
    PENDING = "Pending"
    INPROGRESS = "In progress"
    COMPLETED = "Completed"
    