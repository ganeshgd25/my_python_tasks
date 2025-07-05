

s1 ={2,6,1,15,4,3,8,-3,18,16,23,21,"ganesh"} 
s2= {5,7,8,9,2,6,3,8,21,"ganesh"}


print(s1)
print(type(s1))

s1.add(9)
print(s1)

s1.add(4)
print(s1)

print(len(s1))

s1.remove(8)
print(s1)


print("intersection" ,s1.intersection(s2))

print("union :" ,s1.union(s2))

print("Difference" ,s1.difference(s2)) 

print(4 in s1)

s1.discard(-3)
print(s1)                # first remove and then print

