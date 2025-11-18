#sets and tuples examples 
#set examples
set1={1,2,3,4,5}
print(set1)
print(type(set))
set1.add(6)
print(set1)
set1.remove(2)
print(set1)
#sets automatically delete duplicates
set2={"apple", "banana", "cherry", "cherry"}
print(set2)
#sets are unordered while lists and tuples are 
#sets do not have set positions or indexes
#you can modify a list after creation but not a tuple
#sets can also be modified so you can change them but not update a specific item
#sets are ideal to store unchangeable values
tuple1=(1,2,3,4,5)
print(tuple1)
print(type(tuple1))

social_security_number=(123444, 4444445, 5676789)
print(social_security_number)