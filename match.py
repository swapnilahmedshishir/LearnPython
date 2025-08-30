day = 7
match day:
    case 1:
        print('This is a Monday')
    case 2:
        print('this is a Tuesday')
    case 3:
        print("This is a wednesday")
    case 4:
        print("This is a Thursday")
    case 5: 
        print('This is a Friday')
    case 6: 
        print("This day is Saturday")
    case 7: 
        print("This Day is the sunday")


match day: 
    case 1|2|3|4|5:
        print("Today is a weekday")
    case 6|7:
        print("I love Weekends!")