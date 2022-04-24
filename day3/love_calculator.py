# To work out the love score between two people:

#     Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."

# e.g.

# name1 = "Angela Yu"

# name2 = "Jack Bauer"

# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."


fname =  input("Enter your name : ").lower()
sname = input("Enter thier name : ").lower()

count1 = 0
count2 = 0
for character in fname:
    if character in "true":
        count1 += 1
    if character in "love":
        count2 += 1
for character in sname:
    if character in "true":
        count1 += 1
    if character in "love":
        count2 += 1

score = int(str(count1)+ str(count2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
