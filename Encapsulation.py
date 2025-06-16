class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed # private variable

    def get_speed(self):
        return self.__speed

    def set_speed(self, new_speed):
        self.__speed = new_speed


    def show_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.__speed)


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def show_info(self):
        super().show_info()
        print("Fuel Type:", self.fuel_type)

car = Car("Toyota", 200, "Electric")

print("Initial Speed:", car.get_speed())

car.set_speed(250)

print("Updated Speed:", car.get_speed())

car.show_info()

# Assignment

# Assignment 1

class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

# Create an object of BankAccount
account = BankAccount()

# Deposit 100
account.deposit(100)

# Withdraw 40
account.withdraw(40)

# Print the balance
print("Current balance:", account.get_balance())