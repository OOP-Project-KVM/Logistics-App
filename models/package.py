from models.package_status import PackageStatus
LOCATIONS = ["SYD", "MEL", "ADL", "ASP", "BRI", "DAR", "PER"]
DISTANCE_TABLE = {
    "SYD": {"MEL": 877, "ADL": 1376, "ASP": 2762, "BRI": 909, "DAR": 3935, "PER": 4016},
    "MEL": {"SYD": 877, "ADL": 725, "ASP": 2255, "BRI": 1765, "DAR": 3752, "PER": 3509},
    "ADL": {"SYD": 1376, "MEL": 725, "ASP": 1530, "BRI": 1927, "DAR": 3027, "PER": 2785},
    "ASP": {"SYD": 2762, "MEL": 2255, "ADL": 1530, "BRI": 2993, "DAR": 1497, "PER": 2481},
    "BRI": {"SYD": 909, "MEL": 1765, "ADL": 1927, "ASP": 2993, "DAR": 3426, "PER": 4311},
    "DAR": {"SYD": 3935, "MEL": 3752, "ADL": 3027, "ASP": 1497, "BRI": 3426, "PER": 4025},
    "PER": {"SYD": 4016, "MEL": 3509, "ADL": 2785, "ASP": 2481, "BRI": 4311, "DAR": 4025}
}


def get_distance(start_location, end_location):
    return DISTANCE_TABLE[start_location.upper()][end_location.upper()]

## TODO update status if package is delivered


class Package:
    all_ids = set()
    customer_info = {}

    def __init__(self, id_pack, start_location: str, end_location: str, weight: float, customer_contact: str):
        self.validate_id(id_pack)
        self.validate_location(start_location)
        self.validate_location(end_location)
        self.validate_weight(weight)
        self.validate_customer_contact(customer_contact)
        self.validate_locations(start_location, end_location)

        self._id = id_pack
        self._start_location = start_location
        self._end_location = end_location
        self._weight = weight
        self._customer_contact = customer_contact
        self.distance = get_distance(start_location, end_location)
        self.pack_status = PackageStatus.TOBEASSIGNED
        self.expected_arrival_time = None

        Package.all_ids.add(id_pack)
        Package.customer_info[id_pack] = customer_contact

    def set_expected_arrival_time(self, arrival_time):
        self.expected_arrival_time = arrival_time

    @property
    def id(self):
        return self._id

    @property
    def start_location(self):
        return self._start_location

    @start_location.setter
    def start_location(self, value):
        self.validate_location(value)
        self.validate_locations(self._end_location, value)
        self._start_location = value

    @property
    def end_location(self):
        return self._end_location

    @end_location.setter
    def end_location(self, value):
        self.validate_location(value)
        self.validate_locations(self._start_location, value)
        self._end_location = value

    @property
    def weight(self):
        return self._weight

    @property
    def customer_contact(self):
        return self._customer_contact

    @customer_contact.setter
    def customer_contact(self, value):
        self.validate_customer_contact(value)
        self._customer_contact = value

    def validate_id(self, id_pack):
        if not id_pack:
            raise ValueError("You must provide ID")
        if id_pack in Package.all_ids:
            raise ValueError(f"Shipment ID {id_pack} already exists.")

    def validate_location(self, location):
        if location[:3].upper() not in LOCATIONS:
            raise ValueError("We don't provide services at this location.")

    def validate_weight(self, weight):
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number.")

    def validate_customer_contact(self, customer_contact):
        if not 5 <= len(customer_contact) <= 20:
            raise ValueError("Customer contact info  must be between 5 and 20 characters!")

    def validate_locations(self, start_location, end_location):
        if start_location.upper() == end_location.upper():
            raise ValueError("The start and end address must be in different locations.")

    def __str__(self):
        return (f"Package Details:\n"
                f"ID: {self.id}\n"
                f"From: {self.start_location}\n"
                f"To: {self.end_location}\n"
                f"Distance: {self.distance}km\n"
                f"Weight: {self.weight} kg\n"
                f"Status: {self.pack_status.value}\n"
                f"Customer Contact: {self.customer_contact}")

