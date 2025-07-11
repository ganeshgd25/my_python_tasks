
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

# print("recusrion Example results: ")
# tri_recursion(6)


 # k=6  then condition match 6>0  result = 6 + tri_recursion(5)

 # but solve tri_recursion(5) we first need to know ehat is 
 # so the function called itself again

 # then k=5  -- result = 5 + tri_recursion(4)
 # calls tri_recursion(4)

 # keep going 
 # tri_recursion(4) -- 4 + tri_recursion(3)
 # tri_recursion(3) -- 3 + tri_recursion(2)
 # tri_recursion(2) -- 2 + tri_recursion(1)
 # tri_recursion(1) -- 1 + tri_recursion(0)

 # base case k=0 -- result = 0

# tri_recursion(1) = 1 + 0 = 1 → print(1)
# tri_recursion(2) = 2 + 1 = 3 → print(3)
# tri_recursion(3) = 3 + 3 = 6 → print(6)
# tri_recursion(4) = 4 + 6 = 10 → print(10)
# tri_recursion(5) = 5 + 10 = 15 → print(15)
# tri_recursion(6) = 6 + 15 = 21 → print(21)

# output 
# 1
# 3
# 6
# 10
# 15
# 21


# The function keeps calling itself with smaller k until k = 0

# Then it starts coming back up, adding values

# Finally, each result is printed step-by-step 


