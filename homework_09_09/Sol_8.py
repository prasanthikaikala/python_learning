"""
8. BMI calculation: take required parameters for BMI calculation
from the user and calculate BMI of the person.
"""

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height/100)**2

print("Your BMI is %.2f"%(bmi))

