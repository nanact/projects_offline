class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100 

class Bus(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def fare(self):
        total_fare = super().fare()
        total_fare += total_fare * 0.1
        return total_fare

bus = Bus("City Bus", 50)
print(f"Total fare for {bus.name} with capacity {bus.capacity} is: {bus.fare()}")
