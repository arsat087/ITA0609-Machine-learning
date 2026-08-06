from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

X = [[2,50],[3,60],[4,65],[5,75],[6,80],[7,85]]
y = [0,0,0,1,1,1]

model = LogisticRegression()

model.fit(X,y)

pred = model.predict(X)

print("Confusion Matrix:")
print(confusion_matrix(y,pred))
 
print("Accuracy:")
print(accuracy_score(y,pred))

h = int(input("Enter Hours: "))
a = int(input("Enter Attendance: "))

result = model.predict([[h,a]])

print("Result:", "Pass" if result[0]==1 else "Fail")
