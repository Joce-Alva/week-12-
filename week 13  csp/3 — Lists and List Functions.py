# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# collections are used to store multiple items in a single variable 
#lists are ordered collections of items
#lists are mutable, meaning you can change their content 
#lists are created using brackets 
# my_list= [1, 2, 3, 4, 5] #defines list 
# print(my_list)
# print(type(my_list))
# #ACESSING ELEMENTS 
# print(my_list[0]) #1
# print(my_list[1:4])#
# print(my_list[0:])
# print(my_list[-1])
# my_list.append(6) #modifying the list 
# my_list.append(7)
# my_list.append(8)
# my_list.extend([9,10,11,12,13,14,15])
# #add 500 more numbers
# my_list.extend(list(range(15,515)))
# my_list.extend(list(range(515,1116)))
# print(my_list)
# # #instead of creating many varaibles you can store them in a list
# new_list=['a', 'b', 'c']
# new_list.append('d')
# print(new_list)

# #removing an item from the list
# removes_item=new_list.pop()
# print(removes_item)
# print(new_list)
# remove_second_item=new_list.pop(1)
# print(remove_second_item)
# print(new_list)

# #sorting numbers 
# numbers=[4,1,3,2]
# numbers.sort()
# print(numbers)

# #reversing the list 
# numbers.reverse()
# print(numbers)

# #insert values
# numbers.insert(2,10)
# print(numbers)


# third_list=[7,8,9]
# third_list[0] =6
# third_list [-1]=10
# print(third_list)

#this will print out random values
import random
random_list=random.sample(range(1,1000)100)
print(random_list)
print(sorted(random_list))
sorted_list=sorted(random_list)
#reverse the list

#Remove every third item 
#This makes our job easier when we need to manage multiple items 
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
#summary pof list functions 
#.append9item)- adds an item to the end of the list
#.pop(index)-removes and returns the item at a specified index 
#.sort()- sorts the list
#.reverse()-reverses order of the list