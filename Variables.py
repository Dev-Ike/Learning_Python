name = "John" #String
age = 18 #Integer
height = 7.5 #Float
is_student = True #Boolean

print(name)
print(age)
print(height)
print(is_student)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

a = b = c = 10
print(a)
print(b)
print(c)

name, age, height, is_student = "John", 18, 10.5, True
print(name)
print(age)
print(height)
print(is_student)



#Assignment

#Assigment 1
current_year = 2025
birth_year = int(input("What is your birth year?"))
age = current_year - birth_year
print("You are " + str(age) + "years old.")

#Assigment 2
first_name = input("What is your first name?")
last_name = input("What is your last name?")
print("Hello " + first_name + " " + last_name + "!" + " Welcome to Python Programming.")

#Assignment 3
kilometers = float(input("What is your distance in km?"))
miles = kilometers * 0.621371
print("Your distance in miles is " + str(miles))

