#calculate count of item in odd index
list_c=[11,33,44,11,56,78,33,44,99,33,44]
sum1=0
count=0
for i1 in range(len(list_c)):
    if(i1%2==1):
        count+=1
print("count of item in odd index:",count)
