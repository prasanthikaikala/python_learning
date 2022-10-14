ab1=[10,20,40,0,-20,55,0,34,-99,88,66]
count=0

for i in ab1:
    if i <= 0:
        count += 1

print("negative number count = " , count)
