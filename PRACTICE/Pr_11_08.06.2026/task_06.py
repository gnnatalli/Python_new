""" 6. Анализ оценок студентов

Дан список студентов с их оценками по разным предметам.
Напишите программу, которая:
- Вычисляет среднюю оценку для каждого студента.
- Возвращает словарь студентов с их средней оценкой, отсортированный по убыванию оценок.

Данные:
students = [
    {"name": "Alice", "grades": [90, 85, 88]},
    {"name": "Bob", "grades": [78, 81, 75]},
    {"name": "Charlie", "grades": [95, 92, 90]},
    {"name": "Diana", "grades": [88, 84, 82]}
]

Пример вывода:
{'Charlie': 92.33, 'Alice': 87.67, 'Diana': 84.67, 'Bob': 78.0}
"""
students = [
    {"name": "Alice", "grades": [90, 85, 88]},
    {"name": "Bob", "grades": [78, 81, 75]},
    {"name": "Charlie", "grades": [95, 92, 90]},
    {"name": "Diana", "grades": [88, 84, 82]}
]

averages = {student["name"]: sum(student["grades"]) / len(student["grades"]) for student in students}
sorted_averages = dict(sorted(averages.items(), key=lambda student: student[1], reverse=True))

print(sorted_averages)