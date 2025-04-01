class Service:
    def __init__(self, id, route, capacity):
        self.id = id
        self.route = route
        self.capacity = capacity
        self.barges = []

class Barge:
    def __init__(self, id, max_containers, position):
        self.id = id
        self.max_containers = max_containers
        self.current_containers = 0
        self.position = position
        self.service = None 
        self.maintenance = False 
    
    def load_containers(self, quantity):
        space_available = self.max_containers - self.current_containers
        self.current_containers += min(quantity, space_available)
    
    def unload_containers(self, quantity):
        self.current_containers -= min(quantity, self.current_containers)

class ContainerGroup:
    def __init__(self, container_type, quantity):
        self.container_type = container_type
        self.quantity = quantity

class Demande:
    def __init__(self, id, origin, destination, quantity, container_type, request_date, available_date, due_date, priority):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.quantity = quantity
        self.container_type = container_type
        self.request_date = request_date
        self.available_date = available_date
        self.due_date = due_date
        self.priority = priority
