
# ATM withdrawl system

# Intial bank balance is 10000
balance=10000

# This statement ask the user how much amount they want to withdraw 
withdraw_amount = int(input(" please Enter your withdraw amount : "))

# check if the user entered 0 or negative number
# if yes then its invalid because you cant withdraw 0 or negative amount
if withdraw_amount <=0:
    print( "invalid amount please enter a valid 
    amount a positive value.")

# if user entered amount is more then current balance then print insufficient balance
elif withdraw_amount > balance:
    print("Insufficient balance.")

# if both condition are false 
# The amount is valid
# you have enough money
# so proceed to withdraw

else :
    balance -= withdraw_amount 
    print("withdrawal sucessfull , your remaining balance is : " , balance)
# Then print withdraw sucessfull and reamaining balance