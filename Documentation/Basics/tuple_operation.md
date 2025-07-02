
# creating a one tuple and print it.
tuple=(2,4,1,6,1,8,7,9,4,6,1,7,1,4,6,1)
print(tuple)

# create tuple another way and print it.
tuple1= 2,3,5,6
print(tuple1)

# Access the element in tuple with the help of index no 2
print(tuple[2])

# same slicing from index 1 to 3
print(tuple[1:4])

# print len of tuple how manyelements present in tuple
print(len(tuple))

# count how many times 1 appears in tuples.
print(tuple.count(1))

# gives the first index of value is 4 
print(tuple.index(4))

# it will print repeat the tuple 3 times.
print(tuple*3)

# convert tuple into list and print its type
my_lst = list(tuple)

print(type(my_lst))
