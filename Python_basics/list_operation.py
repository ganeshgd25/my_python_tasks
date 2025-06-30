
num = [1,2,3,4,5,2,1,5]

num.append(7)   
print(num)

num.insert(3,10)
print(num)
print(num [2])

print(num.count(1))



str = ["apple","mango","kiwi","banana","khajur"]

str.pop()
print(str)
str.remove("kiwi")             # if you want to remove anything in list so we dont remove to use of index no instead we can remove dierctly 
print(str)    

print(str[2])

lst = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(lst[0], lst[0][1]) 

mix_lst = [1,"mango",3,"apple","ganesh",4]
print(mix_lst)

var = mix_lst[4]
print(var[0].upper())

typ = mix_lst[2]
print(type(typ))





marks = [90,95,20,40,70]
marks.sort()
print(marks)
marks.reverse()
print(marks)

print(marks.index(40))

marks.sort(reverse=True)
print(marks)

print(max(marks))
print(min(marks))
print(sum(marks))

print(sum(marks)/len(marks))    

print(sum(marks)//len(marks))     #avg

r = range(5 , 10)
print(r)