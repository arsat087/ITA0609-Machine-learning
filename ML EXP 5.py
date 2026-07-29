amount = float(input())

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

total = amount - discount
gst = total * 0.18
bill = total + gst

print("Discount =", discount)
print("GST =", gst)
print("Total Bill =", bill)
