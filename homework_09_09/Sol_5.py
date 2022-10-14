distance_in_km = int(input("Enter distance in km:"))

cm = distance_in_km * 100000
meters = distance_in_km * 1000
milli_meters = distance_in_km * 1000000
cents = distance_in_km * 0.621371192#1 kilometer is equal to 0.621371192
feets = distance_in_km * 3280.84#1 kilometer is equal to 3280.84 feet
yards = distance_in_km * 10936.13298# 1 kilometer is equal to 10936.13298 yards
print("%.2f km distance in cm = %.2f"%(distance_in_km, cm))
print("%.2f km distance in meters = %.2f"%(distance_in_km, meters))
print("%.2f km distance in milli meters = %.2f"%(distance_in_km, milli_meters))
print("%.2f km distance in cents = %.2f"%(distance_in_km, cents))
print("%.2f km distance in feets = %.2f"%(distance_in_km, feets))
print("%.2f km distance in yards = %.2f"%(distance_in_km, yards))

