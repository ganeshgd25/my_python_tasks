<!-- 
match case is a pattern matching tool, like switch-case.

case 1|2|3|4|5 means match any of these values.

You can add an if condition inside a case for extra checks (called a guard condition).

_ is used as the default or fallback case.

This example checks:

If it's a weekday in April → prints "a weekday in April".

If it's Saturday/Sunday → prints weekend.

Else → prints "not a valid day. -->



day = int(input("Enter a number (1-7) representing the day of the week: "))

month = int(input("Enter a number (1-12) representing the month: "))

match day : 
    case 1|2|3|4|5 if month==4: print("a weekday in April")
    case 6|7: print("weekend")
    case _: print("not a valid day")




