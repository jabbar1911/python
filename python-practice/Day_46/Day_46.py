# Class with constructor and methods
class Bike:
    # Constructor (__init__)
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        print(f"Bike created: {self.color} {self.brand}")

    # Instance method
    def ride(self):
        print(f"{self.brand} bike is now riding!")

    def repaint(self, new_color):
        self.color = new_color
        print(f"Bike color changed to {self.color}")

# Creating objects (constructor automatically called)
bike1 = Bike("Yamaha", "Red")
bike2 = Bike("Honda", "Blue")

# Calling methods on objects
bike1.ride()          # Output: Yamaha bike is now riding!
bike2.repaint("Black") # Output: Bike color changed to Black
