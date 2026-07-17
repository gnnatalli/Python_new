"""01 Анализ курсов студентов

Реализуйте программу, которая должна:
1. Прочитать файл student_courses.json, содержащий:
    - Имя
    - дату рождения (birth_date) в формате дд.мм.гггг
    - дату поступления (enrollment_date) в том же формате
    - список курсов.

2. Вычислить:
    - общее количество студентов.
    - средний возраст на момент поступления.
    - количество студентов на каждом курсе.

3. Сохранить отчёт в JSON-файл student_courses_report.json.
"""

import json
from collections import Counter
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rld


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_info():
    """
    "name": "Diana Williams",
    "birth_date": "12.06.1983",
    "enrollment_date": "29.04.2023",
    "courses": [
      "Physics",
      "Chemistry"
    ]
    """

    students=read_json("student_courses_1.json")

    total_students=len(students)

    total_age = 0
    courses_counter = Counter()
    for student in students:

        birth_date = dt.strptime(student["birth_date"], "%d.%m.%Y")
        enrollment_date = dt.strptime(student["enrollment_date"], "%d.%m.%Y")

    #     Возраст на момент поступления
        age = rld(enrollment_date, birth_date).years
        total_age += age

        # Подсчет курсов
        courses_counter.update(student["courses"])

    average_age = round(total_age/total_students, 2)

    report = {
        "total_students": total_students,
        "average_age_at_enrollment": average_age,
        "students_per_course": dict(courses_counter)
    }

    write_json("student_courses_report.json", report)

    print("Отчет успешно сохранен в student_courses_report.json")
    print(json.dumps(report, indent=4, ensure_ascii=False))


get_info()