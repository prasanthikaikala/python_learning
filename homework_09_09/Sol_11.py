"""
11. take base and exponent value from the user and print like in mathematics:
  example: base=2, exponent=3: 23
Use: 2\u00b3
"""
base = input("Enter base value: ")
exponent = input("Enter exponent value: ")
exp = eval(r'"\u00b' + str(exponent) + '"')

print(exp)

