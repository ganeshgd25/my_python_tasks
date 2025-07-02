
balance=10000
withdraw_amount = int(input(" please Enter your withdraw amount : "))


if withdraw_amount <=0:
    print( "invalid amount please enter a valid amount a positive value.")
elif withdraw_amount > balance:
    print("Insufficient balance.")
else :
    balance -= withdraw_amount 
    print("withdrawal sucessfull , your remaining balance is : " , balance)
    