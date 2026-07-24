""" 03 Класс Teacher и список людей

На основе класса Person создайте класс Teacher.
- У преподавателя есть имя и предмет.
- Метод introduce() должен выводить имя и предмет.

Метод introduce() должен выводить строку:
    Hello, I am professor <имя>. My subject is <предмет>.

Создайте список, в котором будут Student и Teacher,
и вызовите у всех метод introduce().

Пример вывода:
Hello, my name is Alice.
I'm on course 2.
Hello, I am professor Bob.
My subject is Mathematics
"""

class Person:
    pass


class Student():
    pass


class Teacher():
    pass


student1 = Student("Alice", 2)
teacher1 = Teacher("Bob", "Mathematics")

people = [student1, teacher1]

for person in people:
    person.introduce()

# Hello, my name is Alice.
# I'm on course 2.
# Hello, I am professor Bob.
# My subject is Mathematics