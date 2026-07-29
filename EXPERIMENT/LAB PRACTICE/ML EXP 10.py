age = int(input("Enter Age: "))
tclass = input("Enter Class (First/Second): ")

if tclass == "First":
    fare = 500
else:
    fare = 300

if age < 5:
    fare = 0
elif age <= 12:
    fare = fare * 0.5
elif age >= 60:
    fare = fare * 0.7

print("Ticket Fare =", fare)
