# studself=Noneame": "Rolf", "grades": (89, 90, 93, 78, 90)}
# def average(sequence):
#     return sum(sequence) / len(sequence)
# print(average(student["grades"]))

# to rewrite the previous code of calculating student average score in object-oriented way:
# which is to define a class

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def student_name(self):
        return self.name


student_0 = Student("John", (100, 100, 99, 100, 99))
student_1 = Student("Rolf", (90, 90, 88, 87, 93))
print(student_0.average_grade())
print(student_1.student_name())
