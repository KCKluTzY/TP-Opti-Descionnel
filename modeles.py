class Service:
    def __init__(self, id, route, capacity):
        self.id = id
        self.route = route
        self.capacity = capacity
        self.barges = []

    def __repr__(self):
        return f"Service(id={self.id}, capacity={self.capacity}, route={self.route})"

class Barge:
    def __init__(self, id, max_containers, position):
        self.id = id
        self.max_containers = max_containers
        self.current_containers = 0
        self.position = position
        self.service = None 
        self.maintenance = False 
    
    def load_containers(self, quantity): # Piste d'amélioration pour gérer la quantité
        space_available = self.max_containers - self.current_containers
        self.current_containers += min(quantity, space_available)
    
    def unload_containers(self, quantity): # Piste d'amélioration pour gérer la quantité
        self.current_containers -= min(quantity, self.current_containers)

class ContainerGroup: # Piste d'amélioration pour gérer la quantité
    def __init__(self, container_type, quantity):
        self.container_type = container_type
        self.quantity = quantity

class Demande:
    def __init__(self, id_, capacity, origin, destination, departure_day, desired_time):
        self.id = id_
        self.capacity = capacity
        self.origin = origin
        self.destination = destination
        self.departure_day = departure_day
        self.desired_time = desired_time

    def __repr__(self):
        return (f"Request(id={self.id}, capacity={self.capacity}, origin={self.origin}, "
                f"destination={self.destination}, departure_day={self.departure_day}, "
                f"desired_time={self.desired_time})")