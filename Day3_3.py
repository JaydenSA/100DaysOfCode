print('Welcome to Leap Year Finder Outer. ')

year = int(input('Please enter the year you would like checked: '))
check = 0

if (year % 4 == 0): 
    if (year % 100 == 0):
        print('Leap year')
        exit()
    else: 
        if (year % 400 != 0):
            print('leap year')
        else: 
            print("Not a leap year")
else: 
    print('not a leap year')
