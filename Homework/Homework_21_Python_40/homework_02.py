"""02 Группировка студентов по классам

Создайте структуру для группировки студентов по классам.
Добавьте студентов в соответствующие группы.

Данные:
students = [
    ("class1", "Alice"),
    ("class2", "Bob"),
    ("class1", "Charlie"),
    ("class3", "Daisy")
]

Пример вывода:
{
    'class1': ['Alice', 'Charlie'],
    'class2': ['Bob'],
    'class3': ['Daisy']
}
"""

from collections import defaultdict

def get_students_groups(students):
    # Создаем словарь, где значение по умолчанию - пустой список
    groups = defaultdict(list)
    # Перебираем пары, класс, студент
    for class_name, student in students:
        # Добавляем студента в список соответствующего класса
        groups[class_name].append(student)
    # Преобразовываем defaultdict в обычный dict
    return dict(groups)

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
sample = {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}


print(get_students_groups(students))
print(get_students_groups(students) == sample)