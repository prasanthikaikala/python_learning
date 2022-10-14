city_pins = [500001,110001,220002,330003,110001,220004]
city_names ={500001:"HYD",110001:"ND",220002:"KK",330003:"CH",110005:"ND",220004:"MUM"}
winter_temp={500001:23,110001:9,220002:12,330003:23,110001:10,220004:14}
summer_temp={500001:45,110001:47,220002:40,330003:36,110001:45,220004:44}
population={500001:120000,110001:110000,220002:44444,330003:555555,110001:7777,220004:6666}
for i2 in city_pins:
    res1= "CITY NAME: {}, PINCODE: {} ".format(city_names[i2],i2)
    temp="winter temp : {},summer temp: {},population: {}".format(winter_temp[i2],summer_temp[i2],population[i2])
    print(res1)
    print(temp)
#which city with max temp in summer
summer_temp_values=summer_temp.values()
maximum_summer_temp = max(summer_temp_values)
print("Maximum temp value:",maximum_summer_temp)

for (k,v) in summer_temp.items():
    if v==maximum_summer_temp:
        print("City with max temp:",city_names[k])
        break


#which city with min temp in winter
winter_temp_values=winter_temp.values()
minimum_winter_temp=  min(winter_temp_values)
print("Minimum temp value:",minimum_winter_temp)

for(k,v) in winter_temp.items():
    if v==minimum_winter_temp:
        print("city with min temp:",city_names[k])
        break
    
#which city having maximum population
population_values=population.values()
maximum_population = max(population_values)
print("maximum population:",maximum_population)
for(k,v) in population.items():
    if v==maximum_population:
        print("maximum_population:",maximum_population)
        break
    
#which city with minimum popluation
population_values=population.values()
manimum_population = min(population_values)
print("manimum population:",manimum_population)
for(k,v) in population.items():
    if v==manimum_population:
        print("manimum_population:",manimum_population)
        break
