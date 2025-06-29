
words= input("enter words sepreated by spaces:").split()

longest_word=""

for word in words:
    if len(word) > len(longest_word):
        longest_word=word

print(f"The longest word is :{longest_word}")
print(f"it has {len(longest_word)} characters.")
        