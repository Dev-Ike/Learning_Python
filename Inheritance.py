

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

    def display_vehicle_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def display_car_info(self):
        self.display_vehicle_info()
        print("Fuel Type:", self.fuel_type)


my_car = Car("Toyota", 200, "Electric")
my_car.display_car_info()