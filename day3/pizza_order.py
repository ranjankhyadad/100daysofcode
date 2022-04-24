# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1


size = input("Do you need a S, M or a L pizza?: ")

cost = 0
requirePepperoni = input("Do you need pepperoni? Y or N?: ")
requireCheese =  input("Do you need extra cheese? Y or N?: ")

if size == 'S' or size == 's':
    cost = 15
    if requirePepperoni == 'Y' or requirePepperoni == 'y':
        cost += 2
elif size == 'M' or 'm':
    cost = 20
    if requirePepperoni == 'Y' or requirePepperoni == 'y':
        cost += 3
elif size == 'L' or 'l':
    cost = 25
    if requirePepperoni == 'Y' or requirePepperoni == 'y':
        cost += 3

if requireCheese == "Y" or requireCheese == 'y':
    cost +=1

print(f"Your final bill amount: ${cost}")
