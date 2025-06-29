
text=input("Enter your paragraph:")
#clean and split the text
words=text.lower().split()
#find the total no of words and total no of charecters
total_words= len(words)
total_char =len(text)
#find the longest word and smallaet word
longest_word=max(words, key=len)
shortest_word= min(words, key=len)
#find the no of unique words 
unique_words= set(words)
total_unique= len(unique_words)
#count word frequency 
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

with open("text anlysis report.txt","w") as f:

    f.write("\n Text analyasis report")
    f.write(f"total no of words {total_words} also characters no :{total_char}\n.")
    f.write(f"longest word is : {longest_word} and shortest word is : {shortest_word}\n")
    f.write(f"The unique word is :{unique_words} and the total no of unique words are : {total_unique}\n")

    f.write("\n words frequencies :")
    for word, count in word_count.items():
        f.write(f"{word} -> {count} time (s)\n")

print("Anlysis saved in 'text anlysis report.txt'")

with open("text anlysis report.txt","r") as file:
    content=file.read()

print(f"Here is a content in a file :\n {content}")


print("Thank you everything is working fine!")
