
<!-- 
A dictionary named employee stores names and their salaries.

The for loop goes through each name and salary in the dictionary using .items().

Inside the loop, it checks if the salary is greater than or equal to 13000.

If the condition is true, it prints the employee name and salary with a message.
Output will show only employees who earn 13000 or more. -->


# program
employee = {
    "rahul" : 10000,
    "mahesh" : 12000,
    "ramesh" : 15000,
    "suresh" : 8000,
    "ash" : 17000,
}

for name ,salary in employee.items():
    if salary >= 13000:
        print(f"{name} has {salary} salary which is higher than 13000!")