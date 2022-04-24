# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

current_age = int(input("What's your age?: "))

days = 90*365 - current_age*365
weeks = 90*52 - current_age*52
months = 90*12 - current_age*12

print(f"You have {days} days, {weeks} weeks and {months} months left to live")