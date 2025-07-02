

# Arithmetic  Operator
# creating varaibles 
a =10
b =15

# perfrom addition
c = (a+b)
print(c)

# perform substraction
d= (b-a)
print(d)

# perform multiplication
e= (a*b)
print(e)

# perform Division
f=(a/b)
print(f)

# perform floor Division
g=(b//a)
print(g)

# perform modulus
s= (b%a)
print(s)

# perform expoentiation
n=(a**b)
print(n)

# Assignment Operator 

h = 5
h += 3
print(h)

# other Assignment operators include (-== *= /= etc )which work similiar 


# comaparision operator 

x=5
y=7

print(x==y)     # equal 

print(x!=y)     # not equal 

print(x>y)      # greater than

print(x<y)      # less than

print(x>=y)     # greater than equal 

print(x<=y)     # less than equal 


# Logical operators 

p = 15
m =10 

# if both condition match then it will give true (and)
print(p>m and m<p)        

# one of the condition match then it gives True (or)
print(p>m or m>p)          

# if both condition are match also it gives reveresd output false (not)
print (not(p>m and m<p))   


# identity operator 
abc = 5
xyz = 5

# checks if two variables point to different objects in memory.
print(abc is not xyz) 

# checks if two variables point to the same object in memory.
print (abc is xyz)

# membership operator 
lst =[1,2,3,6,4,8]


# Returns true if the value exists in the sequence
print(6 in lst)
print(9 in lst)

# Return True if the value does not exits in sequence.
print(6 not in lst)
print(9 not in lst)

