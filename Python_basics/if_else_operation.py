
age = int(input('Enter your age : '))

if age <= 12:
    print("you are child ")

elif age >= 12 and age<= 19:
     print("you are teenager")

else:
     print("you are adult ")


number = 10

if number >=5 :
     print("No is greater than 5.")
else:
     print("No is not greater than 5.")

age= int(input("plese Enter your age: "))

if age >=18 :
     card=input("Do you have voter card? yes/no ").lower()
     if card =="yes":
          print("You are eligibale for vote it.")
     elif card == "no":
          print("you are not eligiable for voting.")
else:
     print("you will be eligible for voting after complete your age 18.")

 
marks = int(input("plese enter your marks : "))

print("your marks is : " ,marks)

if marks>=81 and marks <=100:
     print("Congrats your grade is A ")
elif marks >=60 and marks<=80:
     print(" Congrats your grade is B")
elif marks >=35 and marks<=60:
     print("your grade is c")
else:
     print("sorry to say but you are fail.")


lst =[4 , 6 , 8, 3 ,1, 9]

if 4 in lst:
     print("4 is present inside a list")
else:
     print("4 is not present in list")

if 4 not in lst:
     print(" This condition is True ")
else:
     print(" false")