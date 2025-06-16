class Car:

    location = "Europe"

    def __init__(self, wheels, engine, color):
        self.wheels = wheels
        self.engine = engine
        self.color = color

    def display_info(self):
        print("Car Wheels:", self.wheels)
        print("Car Engine:", self.engine)
        print("Car Color:", self.color)



bmw = Car(4, "Hybrid", "Blue")
ferrari = Car(4, "Fuel", "Red")

bmw.display_info()
ferrari.display_info()

bmw.seats = 2

ferrari.gears = 9
ferrari.speed = 350

print(f"BMW - Seats: {bmw.seats}")
print(f"Ferrari - Gears: {ferrari.gears}, Speed: {ferrari.speed}")


print("Location BMW", bmw.location)
print("Location Ferrari", ferrari.location)