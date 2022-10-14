gb = int(input("Enter disk size in GB:"))

mb = gb * 1024
kb = mb * 1024
tb = gb * 0.0009765625
pb = gb * 0.00000095367432

print("%s GB size in MB = %s"%(gb, mb))
print("%s GB size in KB = %s"%(gb, kb))
print("%s GB size in TB = %s"%(gb, tb))
print("%s GB size in PB = %s"%(gb, pb))


