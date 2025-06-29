# my_python_tasks

# Notes for Day_01 29jun-2025

# Dictionary Declaration 
book= {

    "title" : "python basics",
    "author": ["Ganesh Deshpande", "Hansraj Deshpande", "Ashish more", "Rushi Shinde"],
    "year" : "2024",
    "intro": "this book is written on python basics ***",
  }
  
 # creating a one dictionary named book that hold the deatils
# "title" : a string 
# "author" : a list of names
# "year" : publication year
# "intro" : Description of book.

 
# print the title and author of the book 
print(f"Title of the book is : {book ['title']} and author of the book is : {book ['author']}")
# fetched and display the book and list of author 


# Get first word of title
print(f"Title of the book is : {book ['title'].split()[0]}") 
# split() use -- its split string by spaces into list of words
#  .split() -- turns "python basics " -- ['python','basics']
#   [0] if index no 0 then then it will fetch first item that is python.


# print authors
print(f"Author of the book is : { book['author'][:]}") 
# if we use [:] -- Then it will print all authors
# if we use [1:2] -- Then it will start from index no 1 and excluded last and print just before index 2 
# if we use [1:3] -- Then it will start from 1 and excluded last means it will print only just bedore index no 3


# Remove extra spaces in intro
print(f"intro for the book is : {book ['intro'].strip()}")
#  Removing leading and trailing spaces 
# string method : .strip()
# string.strip("*") it removes all leading and trailing stars only from ends not in middle main uses it removes the white space but only start and end not from middle

# convert intro into the uppercase
print(f"intro for the book is : {book ['intro'].upper()}")
# convert into to all capital letters
# The operation is .upper()

# convert Lowercase the intro 
print(f"intro for the book is : {book ['intro'].lower()}")
# converts all charcters to lowercase
# The operation  is .lower()

# Title case intro 
print(f"intro for the book is : {book ['intro'].title()}")
# make the first leatter of each word uppercase 
# The operation is .title()


# capitalize first letter only
print(f"intro for the book is : {book ['intro'].capitalize()}")
# only first letter is capitalized 
# The operation is .capitalize() 

# Replace word in intro 
print(f"intro for the book is : {book ['intro'].replace("basics","advance")}")
# Replace the word basics into advance 
# The operation is .replace("old" , "new")

# find index for given value 
print(f"intro for the book is : {book ['intro'].find("w")}")
# search for 'w' and return its index no 
# The operaton is .find('char') return its postion.
# if the char is present it returns index 
# if the char is not present it returns -1 

# find index of given value (gives error if not found)
print(f"intro for the book is : {book ['intro'].index("w")}")
# same as .find() but gives the error if char is not found
# The operation is .index('char')
# if the char is present it returns index
# .index() raises an error if char is not found.

# check if intro starts with that 
print(f"intro for the book is : {book ['intro'].startswith("that")}")
# if it is starts with that then return True else return false
# syntax :  .startswith('text")

# check if intro ends with **
print(f"intro for the book is : {book ['intro'].endswith("**")}")
#  if it is ends  with that then return True else return false
# syntax : .endswith('text')

# wrong syntax 
print(f"intro for the book is : {book ['author'].len()}")

# .len() is not a method it is built in function thats why gives error 

# instead of we use syntax 
#   print (f"intro for the book is : {len(book['author'])}")
# it will gives the no of authors


# update the year 
 book['year']=2025 
 print(f" updated year is : {book['year']}")
 
# update the year
book.update({"year":2026})
print(f" updated year is : {book['year']}")
# channge the year from 2024--2026
# syntax -- .update()

# delete author
del book["author"]
# its removes the author 
# syntax -- del dict_name['key']

# print the updated dictionary
print(f" updated dict : {book}")

# final output  --- 
 updated dict : {'title': 'python basics', 'year': 2026, 'intro': 'this book is written on python basics ***'}

# opearions                             # its use or purpose

# book['key'] 	                         Access dictionary value
# .split()                               Split string into list
# [:]	                                 List slicing
# .strip()	                             Remove spaces
# .upper() / .lower()	                 Change case
# .title() / .capitalize()               Format text
# .replace()	                         Replace part of string
# .find() / .index()	                 Search character
# .startswith() / .endswith()	         Check beginning or end
# len(list)                              Get count
# .update()                              Change value in dictionary
# del	                                 Remove key from dictionary


# why you are using the 'f' in print statement 
# Ans is ---- 
             f-string its allows the insert varaibles expression dierctly inside the curly braces{}
             ex--- name="Gd"
                   print(f"my name is {name}")
# without f string old way 
            ex --name ="gd"
                 print("my name is " +name)
                 # need to use + to join string
                 # be diffcult for many varaible
# why use f string 
 clean syntax
 easier to read and maintain 
 supports varaibles ,math functions call dierctly inside the {} .
