
word="banana"
count_dict= {}

for char in word:
    if char in count_dict:
        count_dict[char] +=1
    else:
        count_dict [char]=1

print(count_dict)