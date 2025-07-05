
bill_amount = float(input("Enter your bill amount : "))

if bill_amount >= 10000:
    discount = 10 

elif bill_amount >= 5000:
    discount = 5 

else:
    discount = 0


discount_amount = (discount / 100 ) * bill_amount 
print("Discount_amount is : " ,discount_amount)

final_amount = bill_amount -discount_amount
print("final amount is : " , final_amount)