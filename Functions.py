# Definition

def say_hello():
    print("Hello World!")

#say_hello()


def greet(name):
    print("Hello", name)

#greet("Alice")
#greet("Bob")
#greet("Charlie")


def add(a, b):
    print("Sum: ", a + b)

#add(3, 5)


def greet(name = "Guest"):
    print("Hello", name)

#greet("Alice")
#greet()

def square(num):
    return num * num

result = square(4)
print("Square of 4 is: ", result)


# Assignment

# Assignment1
def add_numbers(a, b):
    return a + b


# Assignment2
def is_even(num):
    if num % 2 == 0:
        return "This number is even"
    else: return "This number is odd"


# Assignment3
def greet(name = "Guest"):
    return "Hello", name


# Assignment4
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


