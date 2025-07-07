
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