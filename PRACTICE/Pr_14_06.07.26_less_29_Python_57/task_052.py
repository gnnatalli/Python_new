""" 5.2 Распределение задач

Функция task_assigner()
- читает файл tasks.txt
- и назначает задачи сотрудникам по очереди.

Она использует генератор для
- постепенного чтения новых задач
- и назначения этих задач сотрудникам.

Дополнительно: если файл tasks.txt отсутствует,
программа делает 5 попыток с паузой 3 секунды перед завершением:
Файл не найден, попытка 1/5...
Файл не найден, попытка 2/5...
Файл не найден, попытка 3/5...
Файл не найден, попытка 4/5...
Файл не найден, попытка 5/5...
Файл так и не найден. Завершаем работу.


Если же файл задач есть, то задачи распределяются между сотрудниками "по кругу":

Данные:
employees = ["Alice", "Bob", "Charlie"]

Пример вывода:
Alice выполняет: Подготовить отчёт
Bob выполняет: Провести собрание
Charlie выполняет: Проверить документацию
Alice выполняет: Разработать новый модуль
Bob выполняет: Настроить сервер
"""

import time
import itertools
import os


# Генератор с 5 попытками открыть файл
def task_assigner(employees, filename="tasks.txt"):
    attempts = 0

    employee_cycle = itertools.cycle(employees)

    while not os.path.exists(filename):
        attempts += 1
        if attempts == 5:
            print("Файл так и не найден. Завершаем работу.")
            return
        print(f"Файл не найден, попытка {attempts}/5...")
        time.sleep(3)

    with open(filename, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if line:
                yield next(employee_cycle), line
            else:
                time.sleep(3)

if __name__ == "__main__":
    # Запуск генератора
    employees = ["Alice", "Bob", "Charlie"]
    task_generator = task_assigner(employees)

    for task in task_generator:
        employee, task = task
        print(f"{employee} выполняет: {task}")
