 <!-- The sentence is stored in a variable named sentense.

The .split() function is used to break the sentence into a list of words using spaces.

An empty dictionary count is created to store word frequencies.

A for loop is used to go through each word in the list.

Inside the loop, the get() method is used to safely retrieve the current count of each word (defaulting to 0 if the word is not found).

The count of each word is then incremented by 1.

After the loop finishes, the dictionary count contains all words as keys and their number of occurrences as values.

Finally, the print(count) statement displays the word count dictionary.  -->


# program 

sentense = "python is a easy programming language and python is very powerfull programming language "

word = sentense.split() 

count = {}

for words in word :
    count[words] = count.get(words,0) +1

print(count)