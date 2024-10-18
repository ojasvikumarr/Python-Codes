while(True):
    year = input("Enter the year : ")
    year = int(year)
    if(year % 400 == 0) :
        print("This is a Leap Year!!")
    elif(year % 100 == 0):
        print("This is not a Leap Year!!")
    elif(year % 4 == 0):
        print("This is a Leap Year!!")
    else:
        print("This is not a Leap Year!!")

datetime.date.today()