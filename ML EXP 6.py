food = float(input("Enter Food Bill: "))

gst = food * 0.05
service = food * 0.10

total = food + gst + service

print("Food Bill =", food)
print("GST =", gst)
print("Service Charge =", service)
print("Total Bill =", total)
