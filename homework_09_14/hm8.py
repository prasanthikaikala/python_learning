#count howmany negative numbers are there in odd index
list_c=[11,33,44,11,56,78,33,44,99,33,44]
count=0
for i in range(1,len(list_c),2):
    if list_c[i]<=0:
        count+=1
print("negative numbers are there in odd index:",count)
