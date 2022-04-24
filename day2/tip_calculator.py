print("Welcome to tip calculator!")

total =  int(input("What was the total bill?: "))
tip =  int(input("How much percentage do you wanna tip? 10, 12 or 15?: "))
count =  int(input("How many people are there?: "))

bill_after_tip =  total + tip/100*total
cost_per_person = round(bill_after_tip/count, 2)

print(f"Each person has to pay ${cost_per_person}")