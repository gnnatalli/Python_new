""" 02 Класс Student

На основе класса Person создайте класс Student.
- Студент должен иметь имя и номер курса.
- Метод introduce() должен
    - сначала выводить базовое приветствие,
    - а затем строку: I'm on course <номер_курса>.

Пример вывода:
Hello, my name is Alice.
I'm on course 2.
"""


class Person:
    pass


class Student():
    pass


student1 = Student("Alice", 2)
student1.introduce()

# Hello, my name is Alice.
# I'm on course 2.