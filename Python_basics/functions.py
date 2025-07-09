
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



        
