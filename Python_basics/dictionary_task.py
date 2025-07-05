# Create a dictionary called book with the following keys:
# "title": "Python Basics"
# "author": "Ganesh Deshpande"
# "year": 2024
# Then do the following:
# Print the title and author of the book.
# Add a new key "pages" with value 250.
# Update the "year" to 2025.
# Delete the "author" key.
# Print the final dictionary.


book= {

    "title" : "python basics",
    "author": ["Ganesh Deshpande", "Hansraj Deshpande", "Ashish more", "Rushi Shinde","Hansraj Deshpande"],
    "year" : "2024",
    "intro": "this book is written on python basics ***",
    
}

#print the title and author of the book 

print(f"Title of the book is : {book ['title']} and author of the book is : {book ['author']}")

print(f"Title of the book is : {book ['title'].split()[0]}") 
    
print(f"Author of the book is : { book['author'][1:]}")

print(f"intro for the book is : {book ['intro'].strip()}")

print(f"intro for the book is : {book ['intro'].upper()}")

print(f"intro for the book is : {book ['intro'].lower()}")

print(f"intro for the book is : {book ['intro'].title()}")

print(f"intro for the book is : {book ['intro'].capitalize()}")

print(f"intro for the book is : {book ['intro'].replace("basics","advance")}")

print(f"intro for the book is : {book ['intro'].find("x")}")

print(f"intro for the book is : {book ['intro'].index("w")}") 

print(f"intro for the book is : {book ['intro'].startswith("that")}")

print(f"intro for the book is : {book ['intro'].endswith("**")}")

#print(f"intro for the book is : {book ['author'].len()}")

# book['year']=2025 

# print(f" updated year is : {book['year']}")

book.update({"year":2026})

print(f" updated year is : {book['year']}") 

#book["author"].remove("Hansraj Deshpande")

print(f" updated dict : {book}")

#del book["author"] [5] 

#book ["author"].pop(5)

print(f" updated dict : {book}")


if "mahesh" in book["author"] :
    book["author"].remove("mahesh")


print(f" updated dict : {book}")
