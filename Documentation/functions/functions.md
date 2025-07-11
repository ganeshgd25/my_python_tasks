

# Basic function with two parameters.

def function (fname,lname):
    print("hello from function!" + fname +" "+lname)

function("ashish","more")

# print using a full name passed as arguments.

# function with default parameters.

def my_function(fname = "Ganesh", lname = "deshpande"):
    print("Hello from my_function!" + fname + " " + lname)

my_function("ganesh" , "deshpande")
my_function("suresh" , "kumar")
my_function()

# pass the default arguments in a function.if no arguments provided it uses default values

# function with *args (varaible length positional arguments.) arbetric function.

def kids(*kids):
    print("The youngest child is " + kids[2])

kids("Emil", "Tobias", "Linus") 

# use *args arbetric function to accpet the varaible no of arguments print the third child (index no 2)


# function with keyword arguments.

def child(child1, child2, child3):
    print("The youngest child is " + child3)

child(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# uses keyword arguments to pass child name print the youngest third child.


# functions with *kwargs (varaible length keyword arguments.)

def my_function1(**student):
    print("His last name is " + student["lname"])

my_function1(fname = "Ganesh", lname = "deshpande")

# uses *kwargs dictionary of keyword arguments.
# Access the value for key is lname


# functions to loop through a list.
def my_function2(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function2(fruits)

# loops through the list and print each item in a list.


# functios to print alternate even index elemts in tuple.

def my_function3(tuple):
    for i in range(len(tuple)):
        if i % 2 == 0:
            print(tuple[i])

tuple= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
my_function3(tuple)

# print elements at even indices in a tuple using loop and if i%2==0


# functions that return a value

def my_function4(x):
    return 5*x

print(my_function4(4))
print(my_function4(2))
print(my_function4(6))

# Return 5 time value of x demonstrate return statement.


# empty function with pass

def my_function5():
    pass

my_function5()

# A placeholder function using pass no operation is performed.
        


# postional only argument 

def my_function6(x , /) :
   print(x) 
my_function6(5)                    # in postional only we can pass only postion if try x=5 then give error 


# keyword only argument

def my_function7(*, a) :
    print(a)

my_function7(a=9)                # in keyword only we can pass value a=9 if pass only 9 then give error


# postional and keyword arguments

def my_function8(a , / , * , b) :
    print(a,b)
                                            
my_function8(10,b=19)               # both mixed postional and keyword only postion also passed and keyword also