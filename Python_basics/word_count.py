
sentense = "python is a easy programming language and python is very powerfull programming language "

word = sentense.split()

count = {}

for words in word :
    count[words] = count.get(words,0) +1

print(count)