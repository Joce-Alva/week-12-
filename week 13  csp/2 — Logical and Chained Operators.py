# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True

#score calculator 
score= int(input("Enter your score (0-100)"))
# An a is 90 to 100
if 90 <= score <=100:
    print("Grade: A")
# A B is a 80 to 89 
elif 80 <= score < 90: 
    print("Grade: B")
# A C is a 70 to 79
elif 70 <= score < 80:
    print("Grade: C")
# A d is a 60 to 69
elif 60 <= score < 69:
    print("Grade: D")
# Anything below is a F 
else:
    print("Grade: F")
# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
number= int(input("Enter a number: "))
if 50 <= number <= 100:
    print("Your number is between 50 and 100")
else:
    print('Your number is not between 50 and 100')
# Write an expression that checks if a number is NOT equal to 0 and greater than 10.
number2= int(input("Enter a number:"))
if number2 >= 10:
    print("Your number is greater than 10")
if number2 <= 0:
    print("Your number is not greater than 10")

# Use chained comparison to check if 3 < 4 < 5.
a=3
b=4
c=5
print(a < b < c)     
# Challenge: Create a password rule using logical operators:

