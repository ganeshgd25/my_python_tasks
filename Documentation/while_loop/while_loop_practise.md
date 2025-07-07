
<!-- 
Program 1: using break
a starts from 1
while a is less than or equal to 10
if a becomes 6, break stops the loop
otherwise, print a
a increases by 1 each time
output will be 1 to 5 -->

# program
a = 1

while a <= 10 :
    if a == 6 :
        break
    print(a)
    a+=1 


<!-- Program 2: using continue
d starts from 0
while d is less than 20
d increases by 1 each time
if d is 11, skip printing and go to next loop
otherwise, print d
output will be 1 to 20, but 11 is skipped -->


# program
d = 0

while d < 20 :
    d+=1
    if d == 11 :
        continue
    print(d) 
    

