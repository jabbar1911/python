# Class as a blueprint
class Vehicle:
    # Class attribute (shared by all objects)
    vehicle_type = "Transport"

    # Instance attributes
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # Method (behavior)
    def show_info(self):
        print(f"{self.color} {self.brand} ({Vehicle.vehicle_type})")

# Object as an instance of the class
car = Vehicle("Toyota", "Red")
bike = Vehicle("Yamaha", "Blue")

# Accessing instance method
car.show_info()  # Output: Red Toyota (Transport)
bike.show_info() # Output: Blue Yamaha (Transport)

# Accessing class attribute directly
print(Vehicle.vehicle_type)  # Output: Transport
