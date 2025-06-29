
# # # #greet user

# # # def greet(name):
# # #     print(f"Hello {name} nice to meet you!")

# # # greet("ganesh")
    
# # #square a number

# # def square(number):
# #     result=number*number
# #     print(f"The square of {number} is : {result}")

# # square(4)
    

# #check the numbers is even or odd 

# def even_odd():
#     num=int(input("please enter your number: "))
#     if num % 2 == 0 :
#         print(f"{num} is even no!")
#     else:
#         print(f"its odd number!")

# even_odd()

# find a largest number of given 3 numbers take a no from user

def large_no():
    num1=int(input("plz enter 1st number: "))
    
    num2=int(input("plz enter 2nd number: "))
    
    num3=int(input("plz enter 3rd number: "))

    largest=max(num1,num2,num3)
    print(f"The largest no is: {largest} ")

large_no()