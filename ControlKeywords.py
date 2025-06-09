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