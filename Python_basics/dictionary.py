
#create a dictionary called student with name roll no and marks

student={
         "name" : "Ganesh",
         "roll_no" : "25",
         "marks" : "90"

}
#print the name and marks
print(f"student name is : {student['name']} and marks : {student['marks']}")

#add grade key
student["grade"]= "A"

#updating the marks
student["marks"]= 95

#delete the roll no key
del student["roll_no"]

#print the final dictionary
print(f"final dictionary is : {student}")