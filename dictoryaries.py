#in dictionary, key must be hashable value:
friend_ages = {"Rolf": 20, "Adam": 28, "Anne": 27}
print(friend_ages["Adam"])

friends = [
    {"name":"Rolf","age": 24},
    {"name":"Adam","age": 28},
    {"name":"Anne","age": 27},
]

#access element in dictionaries
print(friends[2])

student_attendance = {"Rolf":96, "Bob":80, "Anne":100}

#access items in dictionaries in for loop:
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

#if statement with dictionaries:
if "Bob" in student_attendance:
    print((f"Bob: {student_attendance['Bob']}"))
else:
    "Bob is not a student in this class."

#access and calculate the values in dictionaries:
attendance_values = student_attendance.values()
print(f"Average attendence score is: {sum(attendance_values) / len(attendance_values)}")