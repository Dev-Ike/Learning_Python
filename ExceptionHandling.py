#num = 10
#print("Dividing numbers...")
#result = num / 0
#print("Result:", result)


# try exception block

#try:
    # code that might throw an exception
#except Exception Type:
    # code to handle exception


# try:
#     num = 10
#     print("Dividing numbers...")
#     result = num / 0
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else block

try:
    num = int(input("Enter a number"))
    print("You entered:", num)
except ValueError:
    print("Invalid input. Please enter a number")
else:
    print("Great. No error occurred")


# finally block
try:
    num = 10
    print("Dividing numbers...")
    result = num / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute, no matter what")


# Assignment

# Assignment1
try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Dividing by zero is not allowed")


# Assignment2
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numeric values.")


# Assignment3
try:
    num1 = int(input("Enter a number: "))
    print("You entered: ", num1)
except ValueError:
    print("Error: Please enter valid numeric values.")
finally:
    print("Input attempt complete. Thank you!")
