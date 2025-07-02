
# # Task A1: Even or Odd Checker
# # Ask the user for a number and check whether it's even or odd.

number = int(input("please enter the no : "))

 if number %2 ==0 :
     print(f"{number } is even no!")

 else:
    print(f"{number}  is odd no !")



# #  Task A2 – Find the largest among three numbers

# # Problem:
# # Ask the user to enter 3 numbers and print the largest one.

 a,b,c= map(int ,input("Enter number seprated by spaces: ").split())
print(a,b,c)

if a>=b and a>=c :
    print("The largest no is :" ,a)

 elif b>=a and b>=c :
     print("The largest no is :" ,b)
 else:
     print("The largest no is :" ,c )


# # Task A3 – Calculate Average and Give Result
# # 🎯 Problem:

# # Ask the user to enter marks for 5 subjects (out of 100).

# # Calculate the average of the marks.

# # Based on the average, print the result as below:

# # Average Marks	Result
# # 90 – 100	🏆 "Outstanding Performance"
# # 75 – 89	🎉 "Excellent, Keep it up!"
# # 60 – 74	👍 "Good Work"
# # 40 – 59	🙂 "You Passed, Try to Improve"
# # 0 – 39	❌ "Fail, Better Luck Next Time"
# # Any Invalid Input	⚠️ "Invalid marks entered!"





# # Task A4 – Admission Based on Marks and Stream Selection
# # 🔸 Problem Statement:
# # Ask the user to enter marks (out of 100).
# # Based on the marks:

# # If marks are >= 75, ask them to choose a stream:

# # If they enter "science", print "You are eligible for Science stream."

# # If they enter "commerce", print "You are eligible for Commerce stream."

# # Otherwise, print "Invalid stream."

# # If marks are between 50 and 74, print "You are eligible for Arts stream."

# # If marks are < 50, print "Sorry, you are not eligible for admission."

marks = int(input("plese enter your marks out of 100 : "))

if marks>=75 :
     stream= input("please enter you want  to which strem (science/commerce) ").lower()
    if stream == "science" :
      print(" congrats you are eligiable for science  ")
    elif stream == "commerce" :
        print( " congrats you are eligiable for commerce")
     else:
         print(" invalid stream ")
    
 elif marks >50 and marks<74:
     print(" Congrtas you are eligiable for Art stream")

else:
     print("sorry you are not eligiable for admission")



# # Task A5 – Leap Year Checker
# # 📌 Problem Statement:
# # Ask the user to enter a year (like 2024, 2025...) and check whether it is a leap year or not.

 year = int(input("please enter a year : "))

 if year % 4 ==0 :

    if year % 100 == 0:

       if year % 400 ==0:
            print("its a leap year")
else:
           print("its not a leap year ")
     else:
        print("its a leap year")

 else:
     print("its not a leap year ")

# # Task A6 – Student Fee Discount System
# # 🧩 Problem Statement:
# # A school gives discounts on fees based on the student's grade and annual marks.
# # Write a program to ask the user for:

# # Grade (between 1 to 12)

# # Annual percentage (0 to 100)

# # 👉 Based on this, print the fee discount:

# # Grade	Percentage ≥ 90	Percentage 75–89	Percentage 50–74	Below 50
# # 1 to 5	30% discount	20% discount	10% discount	    No discount
# # 6 to 8	40% discount	25% discount	15% discount	    No discount
# # 9 to 12	50% discount	30% discount	20% discount	    No discount


 grade =int(input("please enter your grade in between 1 to 12: "))
 percentage= int (input("please enter your percentage in between 1 to 100 : "))

 print("You entered grade is : ", grade)
 print("You entered percentage is : ", percentage)


if grade < 1 or grade > 12 or percentage < 0 or percentage > 100:
     print("Invalid grade or percentage entered.")

elif grade>=1 and grade <=5:
   if percentage>=90:
        print("congrats you are applicable for 30 percent discount.")
    elif percentage >=75 and percentage<=89:
        print("congrats you are applicable for 20 percent discount")
    elif percentage >=50 and percentage<=74:
        print("congrats you are applicable for 10 percent discount")
   else: 
       print("No discount ")
 elif grade>=6 and grade<=8:
    if percentage>=90:
        print("congrats you are applicable for 40 percent discount")
     elif percentage>=75 and percentage<=89:
         print("congrats you are applicable for 25 percent discount")
     elif percentage>=50 and percentage<=74:
        print("congrats you are applicable for 15 percent discount")
   else:
        print("No discount")

elif grade>=9 and grade<=12:
   if percentage>=90:
        print("congrats you are applicable for 50 percent discount")
     elif percentage>=75 and percentage<=89:
         print("congrats you are applicable for 30 percent discount")
    elif percentage>=50 and percentage<=74:
         print("congrats you are applicable for 20 percent discount")
    else:
        print("No discount.")


# # Task A7 – Classify a triangle based on sides
# # 🔶 Problem:
# # Ask the user to enter 3 side lengths of a triangle. Then print what type of triangle it is:

# # Equilateral Triangle – all sides are equal

# # Isosceles Triangle – any two sides are equal

# # Scalene Triangle – all sides are different

# # Also check if it forms a valid triangle (using triangle inequality rule)


a,b,c = map(int , input("please Enter a three sides of traingle: ").split())

 print(f" you have enter sides of traingale :{a},{b},{c}")

 if (a + b > c) and ( a + c > b) and (b + c > a):
    if a == b == c:
        print("Traingle is equilteral.")
    elif a ==b or b ==c or a ==c:
        print("Traingle is isoscales")
    else:
        print("Traingale is scalene.")
else:
    print("The sides do not form a valid triangle.")
