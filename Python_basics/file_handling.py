
f = open ("C:\\Users\\HP\\Desktop\\ganesh.txt", "r")
print(f.read())
f.close()


f = open ("C:\\Users\\HP\\Desktop\\ganesh.txt", "r")
print(f.readline())
print(f.readline())
f.close()



f = open ("C:\\Users\\HP\\Desktop\\ganesh.txt", "r")
lines = f.readlines()
print(lines)
f.close()


with open ("C:\\Users\\HP\\Desktop\\ganesh.txt", "r") as f :
    data = f.read()
    print(data)



with open ("C:\\Users\\HP\\Desktop\\ganesh.txt", "r") as f:
    text = f.read()
    word_count = len(text.split())
    print("Total words :", word_count)


with open ("C:\\Users\\HP\\Desktop\\ganesh.txt", "w") as f:
    f.write ("This is new text \n")
    f.write("python is little bit easy comapring to other lang.\n")


f = open ("C:\\Users\\HP\\Desktop\\ganesh.txt", "r")
print(f.read())


with open ("C:\\Users\\HP\\Desktop\\ganesh.txt", "a") as f:
    f.write("The end of statement..!\n")

f = open ("C:\\Users\\HP\\Desktop\\ganesh.txt", "r")
print(f.read())