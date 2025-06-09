# Break

# Stop the loop immediately


movies = ["Inception", "The matrix", "Interstellar", "Titanic"]
for movie in movies:
    print("Now watching:", movie)
    if movie == "Interstellar":
        print("Found my favourite movie! stopping the marathon")
        break



# Continue
# Skip remaining code in the current iteration

dishes = ["Pasta", "Spicy Curry", "Salad", "Spicy Noodles"]
for dish in dishes:
    if "Spicy" in dish:
        print("Skipping:", dish)
        continue
    print("Eating:", dish)


# Pass
# placeholder for possible future logic

tasks = ["Clean the room", "Skip"]
for task in tasks:
    if task == "Skip":
        pass
    else:
        print("Doing task:", task)

# Assignment

# Assignment1
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print(num1, "is greater")
elif num2 > num1 and num2 > num3:
    print(num2, "is greater")
else: print(num3, "is greater")

# Assignment2
for number in range(1, 21):
    if number % 2 != 0:
        continue  # Skip odd numbers
    print(number)

# Assignment3
num = int(input("Enter the number: "))
if num >= 10 and num <= 50:
    print("number is between 10 and 50")
else:
    print("number is not between 10 and 50")

# Assignment4
numbers = [12, 15, 22, 29, 35, 42, 50]

for num in numbers:
    if num % 7 == 0:
        print("First multiple of 7 found:", num)
        break

# Assignment5
num = 10

while not num == 0:
    print(num)
    num -= 1