
lst = ["ganesh","apple","mango","ash","rushi","kiwi"]

for i in lst :
    if i == "rushi":
        break
    print(i)


# loop starts from 1 to 9
# when i==5 the break staement runs and loop stops immeditaly.
# so it does not print 5 or any number after it.
for i in range(1,10) :
    if i == 5:
        break
    print(i)