# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# collections are used to store multiple items in a single variable 
#lists are ordered collections of items
#lists are mutable, meaning you can change their content 
#lists are created using brackets 
my_list= [1, 2, 3, 4, 5] #defines list 
print(my_list)
print(type(my_list))
#ACESSING ELEMENTS 
print(my_list[0]) #1
print(my_list[1:4])#
print(my_list[0:])
print(my_list[-1])
my_list.append(6) #modifying the list 
my_list.append(7)
my_list.append(8)
my_list.extend([9,10,11,12,13,14,15])
#add 500 more numbers
my_list.extend(list(range(15,515)))
my_list.extend(list(range(515,1116)))
print(my_list)
# #instead of creating many varaibles you can store them in a list
# #This makes our job easier when we need to manage multiple items 
# #performance task answer 
# # Examples:
# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.

# # Print the second and last item.

# # Add a new item using .append().

# # Remove the first item using .pop(0).

# # Reverse your list using .reverse().

# # Create a list of 3 lists (matrix), and access the middle element.