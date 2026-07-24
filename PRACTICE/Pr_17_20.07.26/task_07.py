""" 07. Фильтрация студентов по возрасту

Реализуйте метод
filter_by_min_age(students: list[Student], min_age: int),
как способ отобрать из списка студентов только тех, кто старше определённого возраста.

"""
from datetime import datetime
from pprint import pprint




s1 = Student("Alice", "2005-05-10")
s2 = Student.from_string("Bob, 2001-12-03")
s3 = Student.from_string("Bill, 2009-05-15")
students = [s1, s2, s3]

pprint(Student.filter_by_min_age(students, 20))
#
# [Student: Alice, birth_date: 2005-05-10, ID: 1,
#  Student: Bob, birth_date: 2001-12-03, ID: 2]