# Income Tax calculator

# Ask the user to enter their income 
# input get value as a string and float it to a decimal number
income = float(input ("please enter your income : "))

# if user income is less then 2.5 lakh then no tax
if income <= 250000 :
    tax =0 

# if user income is less than 5 lakh then tax is 5% only the amount above 2.5L 
elif income <= 500000 :
    tax= (income - 250000) * 0.05 

# if income less than 10 lakh then 5% from 2.5 to 5L and 10% above 5L
elif income <= 1000000 :
    tax = ( 250000 * 0.05) + (( income - 500000) * 0.10)

# if income is greater then 10L 
# 5% on 2.5L
# 10% on 5L to 10L
# 20% on the rest above 10L
else :
    income >= 1000000
    tax = ( 250000 * 0.05) + ( 500000 * 0.10 ) + ( ( income - 1000000 ) * 0.20 )

# Display the calculated tax to user
print ( "Your total calculated income tax is : " , tax) 