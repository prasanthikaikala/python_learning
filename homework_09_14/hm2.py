
#calculate average of the items present at odd index
list_c=[11,33,44,11,56,78,33,44,99,33,44]
sum1=0
count=0
for i1 in range(len(list_c)):
    if(i1%2==1):
        count+=1
        sum1=sum1+list_c[i1]
print(sum1)
avg=float(sum1)/float(count)
print(avg)
                
                
#calculate count of item in odd index
list_c=[11,33,44,11,56,78,33,44,99,33,44]
sum1=0
count=0
for i1 in range(len(list_c)):
    if(i1%2==1):
        count+=1
print("count of item in odd index:",count)


#calculate sum of the items present at multiple of 3 index [0,3,6,9]
list_c=[11,33,44,11,56,78,33,44,99,33,44]
sum1=0
for i in range(len(list_c)):
    if(i%3)==0:
        sum1=sum1+list_c[i]
print(sum1)




#calculate sum of the items starting 0 to 1000
sum1=0
for i in range(0,1000):
 sum1=sum1+i
print(sum1)


# count how many positive number are there in even index
list_c=[11,33,44,11,56,78,33,44,99,33,44]
count=0
for i in range(0,len(list_c),2):
    if list_c[i]>=0:
        count+=1
print("positive number are there in even index:",count)



#count howmany negative numbers are there in odd index
list_c=[11,33,44,11,56,78,33,44,99,33,44]
count=0
for i in range(1,len(list_c),2):
    if list_c[i]<=0:
        count+=1
print("negative numbers are there in odd index:",count)





