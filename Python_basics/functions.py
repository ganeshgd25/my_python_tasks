
def function (fname,lname):
    print("hello from function!" + fname +" "+lname)

function("ashish","more")



def my_function(fname = "Ganesh", lname = "deshpande"):
    print("Hello from my_function!" + fname + " " + lname)

my_function("ganesh" , "deshpande")
my_function("suresh" , "kumar")
my_function()


def kids(*kids):
    print("The youngest child is " + kids[2])

kids("Emil", "Tobias", "Linus") 


def child(child1, child2, child3):
    print("The youngest child is " + child3)

child(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function1(**student):
    print("His last name is " + student["lname"])

my_function1(fname = "Ganesh", lname = "deshpande")


def my_function2(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function2(fruits)


def my_function3(tuple):
    for i in range(len(tuple)):
        if i % 2 == 0:
            print(tuple[i])

tuple= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
my_function3(tuple)


def my_function4(x):
    return 5*x

print(my_function4(4))
print(my_function4(2))
print(my_function4(6))


def my_function5():
    pass
    
my_function5()


# postional only argument 

def my_function6(x , /) :
   print(x) 
my_function6(5)                 # in postional only we can pass only postion if try x=5 then give error 


# keyword only argument

def my_function7(*, a) :
    print(a)

my_function7(a=9)            # in keyword only we can pass value a=9 if pass only 9 then give error


# postional and keyword arguments

def my_function8(a , / , * , b) :
    print(a,b)
                                            
my_function8(10,b=19)                       # both mixed postional and keyword only postion also passed and keyword also



        
