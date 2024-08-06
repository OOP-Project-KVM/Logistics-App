from models.truck import Truck, Status

class Garage:
    '''
    The Garage class is designed to manage a fleet of trucks for a transportation company. It initializes a list of trucks
    based on predefined data, and provides methods to interact with and manage these trucks. The key functionalities include:
    - Initializing the fleet of trucks with specific attributes like model, capacity, and maximum range.
    - Retrieving a list of all trucks or only the available (free) trucks.
    - Finding a specific truck by its unique identifier (ID).
    '''
    
    def __init__(self):
        self.trucks = []
        self.initialize_trucks()

    def initialize_trucks(self):
        truck_data = [
            {'model': 'Scania', 'capacity': 42000, 'max_range': 8000, 'num_vehicles': 10, 'id_start': 1001},
            {'model': 'Man', 'capacity': 37000, 'max_range': 10000, 'num_vehicles': 15, 'id_start': 1011},
            {'model': 'Actros', 'capacity': 26000, 'max_range': 13000, 'num_vehicles': 15, 'id_start': 1026}
        ]

        for data in truck_data:
            for i in range(data['num_vehicles']):
                truck_id = data['id_start'] + i
                truck = Truck(id=truck_id, is_free=Status.AVAILABLE, model=data['model'], capacity=data['capacity'], max_range=data['max_range'])
                self.trucks.append(truck)

    def get_all_trucks(self):
        return self.trucks

    def get_free_trucks(self):
        return [truck for truck in self.trucks if truck.is_free == Status.AVAILABLE]

    