import csv

data = []

with open("trainingdata.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        data.append(row)

specific = data[0][:-1]
general = [["?" for i in range(len(specific))] for j in range(len(specific))]

for row in data:
    if row[-1] == "Yes":
        for i in range(len(specific)):
            if specific[i] != row[i]:
                specific[i] = "?"
                general[i][i] = "?"
    else:
        for i in range(len(specific)):
            if row[i] != specific[i]:
                general[i][i] = specific[i]
            else:
                general[i][i] = "?"

general = [g for g in general if g != ["?" for i in range(len(specific))]]

print("Specific Hypothesis:")
print(specific)

print("\nGeneral Hypothesis:")
for g in general:
    print(g)
