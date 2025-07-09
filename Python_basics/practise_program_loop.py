
num =[1,2,3,4,5]

for i in num:
    if i==3 :
        print("found")
        break 
else:
    print("number not found")


user_database = ["ganesh","rahul","sneha","priya","ash","shanky"]

log_user = input("enter your username: ")

for user in user_database:
    if log_user == user:
        print("Access Granted.")
        break
else:
    print("Access denied.!")


item_lst = [100,500,300,700,110,170]

total_bill = 0

for bill in item_lst:
    total_bill += bill

print(total_bill)



speed_limit =30 

bike_speeds = [10,30,35,52,75,15,18,21,33,41]

over_speed=0

for i in range(10):
    if bike_speeds[i] > speed_limit:
        over_speed+=1

print("speed limit crossed bikes no: ",over_speed)       


