from enum import Enum


class PackageStatus(Enum):
    TOBEASSIGNED = "To be assigned"
    OUTFORDELIVERY = "Out for delivery"
    DELIVERED = "Delivered"
