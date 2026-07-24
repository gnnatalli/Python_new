"""
02. Номер студента
Каждому студенту (объекту student) должен автоматически присваиваться уникальный номер - student_id, начиная с 1.

Этот номер должен храниться в каждом объекте класса Student.
И, разумеется, у каждого студента он должен быть свой собственный.
"""

class Student:
    student_id = 0  # счетчик студентов (атрибут класса)

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

        Student.student_id += 1      # увеличиваем общий счетчик
        self.student_id = Student.student_id  # сохраняем номер в объекте

print(Student.student_id == 0)  # True

s1 = Student("name1", "2000-01-01")
s2 = Student("name2", "2000-01-01")

print(Student.student_id == 2)  # True
print(s1.student_id == 1)
print(s2.student_id == 2)

# True
# True
# True
# True