

# creating a s1 and s2 two sets 
s1 ={2,6,1,15,4,3,8,-3,18,16,23,21,"ganesh"} 
s2= {5,7,8,9,2,6,3,8,21,"ganesh"}

# print set and type of s1 
print(s1)
print(type(s1))   

# add operation perform it will added 9 in set 
s1.add(9)
print(s1)

# 4 is already exists so nothng changes 
s1.add(4)
print(s1)

# it gives the length of set
print(len(s1))

# Remove the element remove 8 from set #first remove then print 
s1.remove(8)
print(s1)

# print the common elements in s1 and s2
print(s1.intersection(s2))

# union print all elements from both sets (no duplicates)
print(s1.union(s2))

# it print values only in s1 not present in s2 
print(s1.difference(s2)) 

# membership operator check the 4 exists in s1 or not -- result will be true or fale 
print(4 in s1)

# remove the value safely if found (not given any error if not found)
s1.discard(-3)
print(s1)                # first remove and then print

# Recap
no duplicate values
unordered
useful for membership testing, removing duplicates and set operation.