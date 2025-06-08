#Sets

my_Set =  {1, 2, 3, 4, 5}

print(my_Set)


#Add

my_Set.add(6)

print(my_Set)


#Remove

my_Set.remove(3)

print(my_Set)


#Union, Intersection and Difference

#Union


set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2

print(union)

#Intersection

intersection = set1 & set2

print(intersection)


#Difference

difference_set1 = set1 - set2

difference_set2 = set2 - set1

print(difference_set1)
print(difference_set2)

#Assignment

#Assignment1
numbers = [10, 25, 8, 99, 3, 67]

print(min(numbers))
print(max(numbers))


#Assignment2
numbers = (2, 5, 3, 5, 8, 5, 10)

target = int(input("Enter a number: "))
count = numbers.count(target)

print("The number " + str(target) + " appears " + str(count) + " times in total." )


#Assignment3
students = {"Alice": 85, "Bob": 78, "Charlie": 92}

#Add
students["John"] = 12
print(students)

#Remove
del students["Alice"]
print(students)


#Assignment4
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2
print(union)

intersection = set1 & set2
print(intersection)

difference_set1 = set1 - set2
print(difference_set1)