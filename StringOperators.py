# String Concatenation (+)
from traceback import print_tb

first_name = "John"
last_name = "Doe"

# full_name = first_name + last_name

full_name = first_name + " " + last_name

print(full_name)


# String Repetition (*)

word = "Hello "
# Repeat 3 times
repeat_count = 3

repeated_word = word * repeat_count

print(repeated_word)


# String Comparison or Relational Operators (==, !=, >, <, >=, <=)

fruit1 = "apple"
fruit2 = "banana"

print(fruit1 == fruit2)
print(fruit1 != fruit2)
print(fruit1 > fruit2)
print(fruit1 < fruit2)
print(fruit1 >= fruit2)
print(fruit1 <= fruit2)


# String Membership Operators (in, not in)

sentence = "The quick brown fox jumps over the lazy dog"

print("quick" in sentence) # True
print("slow" in sentence) # False
print("Quick" in sentence) # False


# String Slicing or Indexing

text = "Hello World!"

# Extract the word Hello from the string text

extracted_string = text[0:5]

print(extracted_string)

# Assignment

# Assignment1
num1 = int(input("Input your first number: "))
num2 = int(input("Input your second number: "))

print(num1 % num2)

# Assignment2
num = float(input("Enter a number: "))

# Check the number and print the result
if num > 10:
    print("The number is greater than 10.")
elif num < 10:
    print("The number is less than 10.")
else:
    print("The number is equal to 10.")

# Assignment3
num = float(input("Enter a number: "))

# Check if the number is between 1 and 100
if 1 <= num <= 100:
    print("The number is between 1 and 100.")
else:
    print("The number is NOT between 1 and 100.")


# Assignment4
num = float(input("Enter a number: "))

# Check if the number is not negative using the not operator
if not (num < 0):
    print("The number is not negative.")
else:
    print("The number is negative.")


# Assignment5
num = float(input("Enter a number: "))

num += 5
num *= 2

print(num)
