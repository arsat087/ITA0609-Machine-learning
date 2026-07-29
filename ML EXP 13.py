vehicle = input("Enter Vehicle Type (Bike/Car): ")
hours = int(input("Enter Parking Duration (Hours): "))

if vehicle == "Bike":
    rate = 20
elif vehicle == "Car":
    rate = 50
else:
    rate = 100

fee = rate * hours

print("Parking Charges =", fee)
