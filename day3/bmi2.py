# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

#     Under 18.5 they are underweight
#     Over 18.5 but below 25 they have a normal weight
#     Over 25 but below 30 they are slightly overweight
#     Over 30 but below 35 they are obese
#     Above 35 they are clinically obese.

weight = float(input("Please enter weight in kg: "))
height = float(input("Please enter height in m: "))\

bmi =  weight/(height*height)

print("Your BMI is "+ str(bmi))

if bmi < 18.5: print("Underweight")
elif bmi > 18.5 and bmi < 25: print("Normal weight")
elif bmi > 25 and bmi < 30: print("Overweight")
elif bmi > 30 and bmi < 35: print("Obese")
elif bmi > 35: print("Clinically obese")