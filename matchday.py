# day = 5
# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")



# day = 4
# match day:
#     case 6:
#         print("today is saturday")
#     case 7:
#         print("today is sunday")
#     case _:
#         print("looking forward the weekend")



# day = 4
# match day:
#     case 1|2|3|4|5:
#         print("today is a weekday")

#     case 6|7:
#         print("i love weekends!")        



month = 4
day = 3
match day:
    case 1 |2 |3 |4 |5 if month == 3:
        print("A weekday in april")

    case 1 |2 |3 |4 |5 if month == 4:
        print("A weekday in may")

    case _:
        print("no match") 