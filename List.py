#List

#syntax
#listname = [element1, element2, element3...]

my_list = [1, 2, 3, 4, 5, "red", "blue", "green", 3]
print(my_list)

#List operations

#Access elements using index
print(my_list[1])
print(my_list[2])
print(my_list[5])

#Append - Use to add elements to a list

my_list.append("House")
print(my_list)

#Remove - Use to remove elements from a list

my_list.remove(3)
print(my_list)

#Retrieve part of a list

print(my_list[1:4])