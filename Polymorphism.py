# Polymorphism in Python

class parentclass:
    # attribute / methods
    pass

class childclass(parentclass):
    # attribute / methods
    pass


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def show_info(self):
        super().show_info()
        print("Fuel Type:", self.fuel_type)

vehicle = Vehicle("Generic Vehicle", 80)
car = Car("Toyota", 200, "Electric")

vehicle.show_info()
car.show_info()




