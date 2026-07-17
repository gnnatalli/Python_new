""" 02 Сумма вложенных чисел

Напишите функцию, которая
- принимает список словарей, где каждый словарь содержит
    - имя пользователя
    - и список баллов.
- Функция должна вернуть сумму всех чисел.
- Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.

Данные:
data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

Пример вывода:
Итоговый балл: 156
"""

from typing import List, Dict, Any

def sum_nested_scores(data: List[Dict[str, Any]]) -> int:

    total = 0

    for user in data:
        total += sum(user["scores"])

    return total
data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]
print(f"Итоговый балл: {sum_nested_scores(data)}")
    
