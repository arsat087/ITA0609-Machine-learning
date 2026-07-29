total = int(input("Enter Total Classes: "))
attended = int(input("Enter Attended Classes: "))

percentage = (attended / total) * 100

print("Attendance Percentage =", percentage)

if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")
