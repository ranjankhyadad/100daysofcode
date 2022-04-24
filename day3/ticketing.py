# Ticketing tool

# Only people > 120 cm height are allowed 
# different tiers : < 12 : $5 , 12-18: $7 and 18+ : $12
# if photo is needed, 3 dollars extra

height = int(input("What's your height in cm?: "))

requirePhotos = False
cost =0

if height > 120: 
    age = int(input("What's your age?: "))
    photos = input("Do you require photos? Y or N? :")
    if age < 12:
        cost = 5
    elif age > 12 and age < 18:
        cost = 7
    elif age > 18:
        cost = 12
    if photos == 'Y' or photos == 'y':
        cost += 3  
        if age < 12: 
            print(f"Please pay ${cost}")
        elif age > 12 and age < 18:
            print(f"Please pay ${cost}")
        elif age > 18:
            print(f"Please pay ${cost}")
    else:
        print(f"Please pay ${cost}")
else:
    print("Sorry! You are not allowed!")
