#calculate sum of the items present at even index
list_c=[11,33,44,11,56,78,33,44,99,33,44]
sum1=0
for i in range(len(list_c)):
    if(i%2)==0:
     sum1=sum1+list_c[i]
print(sum1)


            
