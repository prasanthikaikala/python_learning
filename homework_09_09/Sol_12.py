"""
12. Take some groceries cost prices and print total cost and average cost,
what is the max cost, what is the minimum cost.

"""


# creating an empty list
shopping_item_prices = []
  
# number of elements as input
n = int(input("Enter number of grocery itmes : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    shopping_item_prices.append(ele) # adding the element
      
print(shopping_item_prices)

total = 0

#Calculate sum of prices
for i in shopping_item_prices:
    total = total + i

#Calculate avg
avg = total / len(shopping_item_prices)

print ("Avg price = %.2f"%(avg))

#Calculate max
maximum = max(shopping_item_prices)
print ("Max price = %.2f"%(maximum))

#Calculate max
minumum = min(shopping_item_prices)
print ("Min price = %.2f"%(minumum))
