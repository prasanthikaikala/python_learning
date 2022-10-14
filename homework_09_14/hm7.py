
# count how many positive number are there in even index
list_c=[11,33,44,11,56,78,33,44,99,33,44]
count=0
for i in range(0,len(list_c),2):
    if list_c[i]>=0:
        count+=1
print("positive number are there in even index:",count)
