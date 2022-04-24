my_year = int(input("Enter the year: "))

if my_year % 4 == 0:   
    if my_year % 100 == 0:
        if my_year % 400 == 0:
            print(f"{my_year} is a leap year")
        else:
            print(f"{my_year} is not a leap year")
    else:   
        print(f"{my_year} is a leap year")
else:
    print(f"{my_year} is not a leap year")