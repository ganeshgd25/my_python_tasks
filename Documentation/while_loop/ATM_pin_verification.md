<!-- 
correct PIN is set to 2525

attempt counter starts at 0

maximum 3 attempts are allowed

while attempts are less than 3:
→ ask user to enter the PIN
→ if the entered PIN matches, show success message and break the loop
→ if not, show error and increase attempt by 1
else block runs if all attempts are used without success
→ it prints that the card is blocked -->



# program 

correct_pin = 2525 

attempt = 0

max_attempt =3

while attempt < max_attempt :
    pin = int(input("Enter your pin: "))

    if pin == correct_pin :
        print("pin is correct you can withdraw your money!")
        break
    else:
        print("your entered pin is incorrect..!")
        attempt+=1

else:
    print("your card is blocked.")