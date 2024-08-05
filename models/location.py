

from datetime import datetime

from models.package import LOCATIONS


class Location:
    DATE_FORMAT = "%d-%m-%Y %H:%M:%S"

    def __init__(self, name: str, arrival_time_str: str = None, departure_time_str: str = None):
        self.validate_name(name)
        self._name = name
        self._arrival_time = self.parse_datetime(arrival_time_str) if arrival_time_str else None
        self._departure_time = self.parse_datetime(departure_time_str) if departure_time_str else None
        self.validate_times(self._arrival_time, self._departure_time)

    @property
    def name(self):
        return self._name

    @property
    def arrival_time(self):
        return self._arrival_time

    @property
    def departure_time(self):
        return self._departure_time

    @staticmethod
    def validate_name(name):
        if name[:3].upper() not in LOCATIONS:
            raise ValueError("We don't provide services there.")

    @staticmethod
    def parse_datetime(datetime_str: str) -> datetime:

        try:
            return datetime.strptime(datetime_str, Location.DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Date-time must be in the format '{Location.DATE_FORMAT}'.")

    @staticmethod
    def validate_times(arrival_time, departure_time):
        if arrival_time and not isinstance(arrival_time, datetime):
            raise ValueError("Arrival time must be a datetime object.")
        if departure_time and not isinstance(departure_time, datetime):
            raise ValueError("Departure time must be a datetime object.")

    def __str__(self):
        arrival_str = self._arrival_time.strftime(Location.DATE_FORMAT) if self._arrival_time else 'No arrival expected'
        departure_str = self._departure_time.strftime(Location.DATE_FORMAT) if self._departure_time else 'No departure planned'
        return (f"---Location Details---\n"
                f"Name: {self._name}\n"
                f"Next arrival : {arrival_str}\n"
                f"Next departure : {departure_str}")






