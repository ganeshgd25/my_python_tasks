# tup is a tuple of numbers 
# for i in tup goes through each no one by one 
# print each no on new line.

tup = (2,3,4,1,7,9,11,16,13,14)

for i in tup:
    print(i)


# python is a string that we are looping over charcter by charcter\
# new_text is any empty string whaere we build the new result 
# if the current charcter is p replace with m
# otherwise just add charcter as it is

#text = "python"
new_text = ""

for char in "python":
    if char == "p" :
        new_text += "m"
    else:
        new_text += char

print(new_text)



    

    