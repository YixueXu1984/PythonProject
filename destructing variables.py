#destructing variable
x, y = 5, 11

t = 1,2
a,b = t
print(a,b)

student_attendance = {"Rolf":96, "Bob":80, "Anne":100}

for student, attendance in student_attendance.items():
    print(student, attendance)

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Prince")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

person = ("Bob", 42, "Mechanic")
#use _ as variable names when you don't use this variable
name, _, profession = person
print(name,profession)

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)