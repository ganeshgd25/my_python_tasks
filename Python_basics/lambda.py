
def my_function(n) :
    return lambda a : a * n 

mydoubler = my_function(2)
print(mydoubler(11))

