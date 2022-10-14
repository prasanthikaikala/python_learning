"""
9. name="Jayaram"
age=1.6
height=3.5356234
weight=10.343856783
By using above inputs print the output
Name:Jayaram, Age:1.6, Height:3.54, Weight:10.344
Note: Use format specifiers(%s, %d, %f)

"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

print("Name:%s, Age:%d, Height:%.2f, Weight:%.1f"%(name, age, height, weight))
