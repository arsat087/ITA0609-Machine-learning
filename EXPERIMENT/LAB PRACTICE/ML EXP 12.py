amount = float(input("Enter Recharge Amount: "))

if amount >= 500:
    discount = amount * 0.10
elif amount >= 200:
    discount = amount * 0.05
else:
    discount = 0

final = amount - discount

print("Discount =", discount)
print("Final Recharge Amount =", final)
