
from commands.base_command import BaseCommand
from models.status.truck_status import Status

class ViewFreeTrucksCommand(BaseCommand):
    def __init__(self, params: list[str], app_data):
        super().__init__(params, app_data)

    def execute(self):
        free_trucks = [truck for truck in self.app_data.trucks if truck.is_free == Status.AVAILABLE]
        if not free_trucks:
            return "No free trucks found."
        else:
            return "\n".join(f'{truck.__str__()}' for truck in free_trucks)