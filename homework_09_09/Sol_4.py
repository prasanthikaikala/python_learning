"""
4.take four number from the user (variables name it as x1,x2,x3,x4)
 Do the below operations
 (x1+x2)**2, (x3+x4)**3
variance
standard deviation: sqrt(variance):  User math module. Math.sqrt(variance)
Regression
	y=mx+b
          m=1.23
          b=0.045
          find out y
          y=m*(x1+x2+x3+x4)+b
Find the average of four numbers
Find the sum of four numbers
"""
import math

x1 = int(input("Enter x1:"))
x2 = int(input("Enter x2:"))
x3 = int(input("Enter x3:"))
x4 = int(input("Enter x4:"))

x1_x2 = (x1 + x2) **2

print("(x1+x2)**2 = %d"%(x1_x2))

x3_x4 = (x3 + x4) **3

print("(x3+x4)**3 = %d"%(x3_x4))



"""
Variance calculation
"""
# calculate mean
ls = [x1, x2 , x3 , x4]
m = sum(ls) / len(ls)

# calculate variance
variance = sum((xi - m) ** 2 for xi in ls) / len(ls)

print("Variance = %s"%(variance))

sd = math.sqrt(variance)
print("Standard deviation = %s"%(sd))


m = 1.23
b = 0.045

x = x1 + x2 + x3 + x4

y = m * x + b

print("Using x1=%d, x2=%d, x3=%d, x4=%d , calculated Y =%d"% (x1, x2, x3, x4, y)) 

avg = x/4

print("Using x1=%d, x2=%d, x3=%d, x4=%d , calculated avg =%d"% (x1, x2, x3, x4, avg))

print("Using x1=%d, x2=%d, x3=%d, x4=%d , calculated sum =%d"% (x1, x2, x3, x4, x)) 


