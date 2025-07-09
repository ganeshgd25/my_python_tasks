
day = int(input("Enter a number (1-7) representing the day of the week: "))

month = int(input("Enter a number (1-12) representing the month: "))

match day : 
    case 1|2|3|4|5 if month==4: print("a weekday in April")
    case 6|7: print("weekend")
    case _: print("not a valid day")


