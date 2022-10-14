#accept 5 places in india#
result_1="{}, {}, {}, {}, {}, are in india".format(str("delhi"), str("chennai"), str("mumbai"), str("hyderabad"), str("vijayawada"))
print(result_1)

places=["delhi", "chennai", "mumbai", "hyderabad", "vijayawada"]
result_2="{}, {}, {}, {}, {}, are in india".format(*places)
print(result_2)
#places and pincodes# using tuple#
pincodes = (100001, 200002, 300003, 400004, 500005)
result_3="delhi {}, chennai {}, mumbai {}, hyderabad {}, vijayawada {}, are in india".format(*pincodes)

print(result_3)

result_4="delhi %d, chennai %d, mumbai %d, hyderabad %d, vijayawada %d, are in india"%(100000, 100001, 100002, 100003, 100004)
print(result_4)



result_5="delhi %d, chennai %d, mumbai %d, hyderabad %d, vijayawada %d, are in india"%(pincodes)
print(result_5)
#using title#
result_6=result_5.title()
print(result_6)
#print country and isd codes#
result_7="inida %s, usa %s, canada %s, australia %s, dubai %s, isd codes"%(str("+91"), str("+1"), str("+1"), str("+4"), str("+5"))
print(result_7)

#using upper
result_7="inida %s, usa %s, canada %s, australia %s, dubai %s, isd codes"%(str("+91"), str("+1"), str("+1"), str("+4"), str("+5"))
result_8=result_7.upper()
print(result_8)
#print country and temperatures
result_9="inida %s, usa %s, canada %s, australia %s, dubai %s, celsius"%(str("20c"), str("30c"), str("80f"), str("15c"), str("-20c"))
print(result_9)
result_10=result_9.lower()
print(result_10)



