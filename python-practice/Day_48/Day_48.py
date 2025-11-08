# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"This is a vehicle of brand: {self.brand}")

# Single Inheritance
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def car_info(self):
        print(f"Car Model: {self.model}, Brand: {self.brand}")

# Multilevel Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def battery_info(self):
        print(f"Battery Capacity: {self.battery} kWh")

# Multiple Inheritance
class Flying:
    def fly(self):
        print("This object can fly!")

class FlyingCar(ElectricCar, Flying):
    pass

# Example Usage
ecar = ElectricCar("Tesla", "Model 3", 75)
ecar.info()          # From Vehicle
ecar.car_info()      # From Car
ecar.battery_info()  # From ElectricCar

fcar = FlyingCar("SkyAuto", "X1", 100)
fcar.info()          # Vehicle method
fcar.car_info()      # Car method
fcar.battery_info()  # ElectricCar method
fcar.fly()           # Flying method
