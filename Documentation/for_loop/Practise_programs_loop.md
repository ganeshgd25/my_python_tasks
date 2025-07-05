

# find the no ins list with using for-else
# loop through num list
# if i==3 print found and break the loop
# if the loop finsish and not found 3 then else run print and print no not found.

num =[1,2,3,4,5]

for i in num:
    if i==3 :
        print("found")
        break
else:
    print("number not found")


# check username login
# users enters the name ganesh
# it found it prints "Access granted" and breaks
# if loop ends without finding the name it prints "Access denied..!"

user_database = ["ganesh","rahul","sneha","priya","ash","shanky"]

log_user = input("enter your username: ")

for user in user_database:
    if log_user== user:
        print("Access Granted.")
        break
else:
    print("Access denied.!")


# Calculate total bill from list
# loop through each item price in item_lst
# keep adding each value to total_bill

item_lst = [100,500,300,700,110,170]

total_bill = 0

for bill in item_lst:
    total_bill += bill

print(total_bill)


# count bikes that crossed speed limit
# loop through all 10 bikes speeds
# if bike speed is more than 30 count its as a over speed
# count total no of bikes that croseed the limit.
speed_limit =30 

bike_speeds = [10,30,35,52,75,15,18,21,33,41]

over_speed=0

for i in range(10):
    if bike_speeds[i] > speed_limit:
        over_speed+=1

print("speed limit crossed bikes no: ",over_speed)       