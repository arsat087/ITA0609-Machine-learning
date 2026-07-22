data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

hypothesis = None

for row in data:
    if row[-1] == "Yes":
        if hypothesis is None:
            hypothesis = row[:-1]
        else:
            for i in range(len(hypothesis)):
                if hypothesis[i] != row[i]:
                    hypothesis[i] = "?"

print(hypothesis)
