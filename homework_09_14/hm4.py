#calculate sum of the items present at multiple of 3 index [0,3,6,9]
list_c=[11,33,44,11,56,78,33,44,99,33,44]
sum1=0
for i in range(len(list_c)):
    if(i%3)==0:
        sum1=sum1+list_c[i]
print(sum1)
