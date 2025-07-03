
# Takes the user input bill amount
bill_amount = float(input("Enter your bill amount : "))

# if the bill amont is greater than 10k then discoun is 10%
if bill_amount >= 10000:
    discount = 10 

# if bill amount greater than 5k and less than 10k then discount is 5%
elif bill_amount >= 5000:
    discount = 5 

# if less than 5k then no discount
else:
    discount = 0

# calculate how much discount to substract from total
discount_amount = (discount / 100 ) * bill_amount

# print discount amount
print("Discount_amount is : " ,discount_amount)

# substract discount from final bill
final_amount = bill_amount -discount_amount

# print final amount
print("final amount is : " , final_amount)