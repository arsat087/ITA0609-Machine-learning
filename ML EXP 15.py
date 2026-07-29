temp1 = float(input("Enter Monday Temperature: "))
temp2 = float(input("Enter Tuesday Temperature: "))
temp3 = float(input("Enter Wednesday Temperature: "))
temp4 = float(input("Enter Thursday Temperature: "))
temp5 = float(input("Enter Friday Temperature: "))
temp6 = float(input("Enter Saturday Temperature: "))
temp7 = float(input("Enter Sunday Temperature: "))

temps = [temp1, temp2, temp3, temp4, temp5, temp6, temp7]

print("Maximum Temperature =", max(temps))
print("Minimum Temperature =", min(temps))
print("Average Temperature =", sum(temps) / 7)
