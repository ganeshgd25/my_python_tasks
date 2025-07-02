# Takes marks as input from the user (between 0 and 100).
# Prints the grade according to the following rules:

# Marks	GradeWrite a Python program that:
# 90 - 100	A+
# 75 - 89	A
# 60 - 74	B
# 50 - 59	C
# 35 - 49	D
# 0 - 34	Fail
# Any other	Invalid marks

# marks= int(input("please enter your marks : "))

# if marks >=90 and marks <=100 :
#     print("Congrats your grade is A+..!")

# elif marks >=75 and marks<=89 :
#     print (" Congrats your grade is A..!")

# elif marks >=60 and marks <=74 :
#     print("your grade is B..!")

# elif marks >=50 and marks <=59 :
#     print("your grade is c..!")

# elif marks >=35 and marks <=49 :
#     print("your grade is D..!")

# elif marks >=0 and marks <=34 :
#     print("sorry to say but you have failed..!")

# else:
#     print("sorry invalid marks please Entered marks between 0 to 100 !")


# Task no 2 
# 🎯 Task: Eligibility Checker for College Admission
# 🔸 Problem Statement:

# Write a Python program to check if a student is eligible for college admission based on the following rules:

# ✅ Eligibility Criteria:
# Student must pass all subjects (Maths, Physics, Chemistry).

# Minimum marks in each subject should be >= 35.

# If all marks are above 35:

# If average is >= 75: Print "Eligible for Scholarship Admission!"

# Else: Print "Eligible for Admission without Scholarship."

# If failed in any subject (marks < 35): Print "Not eligible for Admission!"




# Task no 3 

# 🔸 Task : Eligibility for Driving License
# Write a program that asks the user their age, and:

# If age is below 0 or above 120 → Print: Invalid age entered!

# If age is between 0–17 → Print: Not eligible for a driving license.

# If age is 18–60 → Print: Eligible for a driving license.

# If age is 61–80 → Print: Eligible with a medical certificate.

# If age is above 80 → Print: Too old for a new driving license.


age = int(input("Please enter your age: "))

if age < 0 or age > 120:
    print("Invalid age entered..!")
elif age <= 17:
    print("Sorry, not eligible for a driving license..!")
elif age <= 60:
    print("Congrats! You are eligible for a driving license..!")
elif age <= 80:
    print("You are eligible, but you must provide a medical certificate..!")
else:
    print("Sorry, too old for a new driving license..!")