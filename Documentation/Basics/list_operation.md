# All list operation 

 # creating a No list and perfrom operation
num = [1,2,3,4,5,2,1,5]         

# perfrom a append opeartion
num.append(7)                   
print(num)

# when print list then whichever we have passed in append it will added at last.
# num = [1,2,3,4,5,2,1,5,7]

# perform a index operation when we want to insert any value using index give value as well as index no wherever you want to added
num.insert(3,10)
print(num)

# insert the value 10 at index no 3
# [1, 2, 3, 10, 4, 5, 2, 1, 5, 7]

# if you want to print value using index no then 
print(num [2])

#This syntax print the value which are present at index no 2
# value is 3

# if you want to count how many time one charcter appears in the list then we can go with count
print(num.count(1))

# This will print how many time 1 in that list in that case 1 appears 2 times.



# string list operation
# creating a list it conatins fruit names 
str = ["apple","mango","kiwi","banana","khajur"]

# using pop method it removes the last string inside the list 
str.pop()
print(str)
# in that case last string is khajur so it removes it.

# if you want to use remove method we cant use index no with remove with the help of remove we can remove dierctly to give value
str.remove("kiwi")             
print(str)    
# in that case value given kiwi so it will remove kiwi in that list 

# if we wamt to remove the things with the help of index no then there are two options will be there 
1. #using pop 
str.pop(2)
print(str)           # it will remove the value of which ever present at index no 2

2. #using del 
#del.str[3]
print(str)          # it will also remove the value with the help of index no which value is present at index no 3

# Access element which is present at index no 2
print(str[2])


# nested list 
lst = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# use of this print the first row of list and 2nd element because gives the index valu 1
print(lst[0], lst[0][1]) 


# mixed data types string and indexing

mix_lst = [1,"mango",3,"apple","ganesh",4]
# print the full list 
print(mix_lst)

# in that case i want to print value present  at index no 4 then in that want to print first letter and convert that letter into uppercase
var = mix_lst[4]           # stored value in var varaible
print(var[0].upper())      # Then print first char and make it upper

# if you dont want to use etc varaible there then we can make it dierctly

# print(mix_lst[4][0].upper()) # it will print also same.

# create a varaible typ access the element which is present at index no 2
typ = mix_lst[2]
print(type(typ))
# print the type of element which type method which type of element either str or int.




# creating a marks list 
marks = [90,95,20,40,70]

# using sort method we can convert list into ascending order
marks.sort()
print(marks)

# using reverse method we can  reverse the all value
marks.reverse()
print(marks)

# if we want to use index method then it will not print the value present at that index
print(marks.index(40))
# if using index method then we have pass the actual value at it gives at which index this valu is present.

# if you want to print the list in decending order then we have followed the following syntax.
marks.sort(reverse=True)
print(marks)


# print the max value present in list.
print(max(marks))

# print the min value in list
print(min(marks))

# use sum it will give the summation of all no 
print(sum(marks))

# if you want to find avg then use following syntax 
print(sum(marks)/len(marks))    
# if we use (/) then it will gives the output in decimal fromat 63.0 

# if we want to output totally int value not a decmial then instead of use (/) then we can go with (//)
print(sum(marks)//len(marks))     

# print range 
r = range(5,10)
print(r)                            


# Whenever I use l.sort() on one line and print(l) on another line, without storing the result in a variable — how does Python know to print the sorted list? I didn't use sort inside print() or assign it to a variable. Shouldn't it print the original list instead?"

#In Python, the method list.sort() modifies the original list in-place

#It does not return a new sorted list.

#Instead, it changes the content of the existing list itself.

#That's why when you call print(l) after calling l.sort(), the list is already sorted — because the original list has been updated directly.