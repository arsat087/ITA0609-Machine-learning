distance = float(input("Enter Distance (km): "))
mileage = float(input("Enter Mileage (km/l): "))
price = float(input("Enter Fuel Price per litre: "))

fuel = distance / mileage
cost = fuel * price

print("Fuel Required =", fuel)
print("Fuel Cost =", cost)
