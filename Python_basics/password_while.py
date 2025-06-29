
# correct_password="ganesh123"
# attempts=0
# max_attempts=3

# while attempts <max_attempts:
#     password= input("plz enter the password :")

#     if password==correct_password:
#         print("Access granted")
#         break
#     else:
#         print("Incorrect password!")
#         attempts +=1
#         print(f"Attempts left :{max_attempts-attempts}")

#     if attempts==max_attempts:
#         print("Too many failed attempts access denied!")

import time
import getpass

correct_password="gd123"
attempts=0
max_attempts=3

while attempts <max_attempts:
    password=getpass.getpass("plz Enter your password: ")
    
    if password==correct_password:
        print("Access granted welcome to my world : ")
        break
    else:
        attempts +=1
        print(f" Incorrect password Attempts left :{max_attempts-attempts}")
        time.sleep(3)
else:
    print("Too many failed attempts access denied!")
    time.sleep(10)
    print("one last chance ...")

    password=getpass.getpass("plz enter your password again : ")

    if password==correct_password:
     print("Access granted. you made it on last chance!!")
    else:
       print("suspecious Activity ! your Account is blocked sorry for inconvience..!")