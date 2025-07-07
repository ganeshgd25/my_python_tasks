
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