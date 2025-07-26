# 🔁 Task 1: Create a Book class
# Attributes: title, author, year
# Method: get_info() → returns a string like "Title by Author (Year)"

# 🔁 Task 2: Add __str__() so printing the object shows full info.

# 🔁 Task 3: Inheritance Challenge – Vehicle Base Class
# Attributes: brand, model
#
# Method: drive() → print something generic like "Driving a vehicle"
#
# 🔸 Subclass: Car
# Add an attribute: doors
#
# Override drive() → print: "Driving a Car with X doors"
#
# Use super().__init__() in the constructor

# 🔁 Task 4: Polymorphism Practice
# Loop over a list of Vehicle, Car, and maybe Bike — and call .drive() on all of them. Let each return a different result.

# 🔧 Bonus (Encapsulation):
# Create a class BankAccount with:
#
# Private balance: __balance
#
# Method: deposit(amount), withdraw(amount), and get_balance()

# 🔁 Task 1
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(f"{self.title} by {self.author} ({self.year})")

# 🔁 Task 2
    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Year: {self.year}")

# 🔁 Task 3
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        return f"Driving a {self.brand} {self.model} Vehicle"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def drive(self):
        return f"Driving a Car with {self.doors} doors"

# 🔁 Task 4
task_car1 = Car("BMW", "McAlexander", 1)
task_car2 = Car("Toyota", "Camry", 4)
task_car3 = Car("Bugatti", "Chiron", 2)

# 🔧 Bonus (Encapsulation):
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₦{amount}. New balance: ₦{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₦{amount}. New balance: ₦{self.__balance}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.owner}'s account balance is ₦{self.__balance}"

# Testing first class of Book
book1 = Book("My Python Lesson", "John", 2025)
book1.get_info()
print(book1)

# Testing second class of Vehicle
vehicle1 = Vehicle("Lexus", "RX350")
print(vehicle1.drive())

# Testing Vehicle Subclass
car1 = Car("Benz", "C300", 3)
print(car1.drive())

# Testing Task 4
cars = [task_car1, task_car2, task_car3]

for c in cars:
    print(c.drive())

# Testing Bonus Exercise
acct = BankAccount("John", 1000)
acct.deposit(100)
acct.withdraw(100)
print(acct.get_balance())
print(acct)


