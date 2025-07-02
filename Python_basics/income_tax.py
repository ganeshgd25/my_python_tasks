
income = float(input ("please enter your income : "))

if income <= 250000 :
    tax =0 

elif income <= 500000 :
    tax= (income - 250000) * 0.05 

elif income <= 1000000 :
    tax = ( 250000 * 0.05) + (( income - 500000) * 0.10)

else :
    income >= 1000000
    tax = ( 250000 * 0.05) + ( 500000 * 0.10 ) + ( ( income - 1000000 ) * 0.20 )

print ( "Your total calculated income tax is : " , tax) 