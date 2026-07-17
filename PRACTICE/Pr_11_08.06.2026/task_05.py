""" 5. Очередь с ограничением времени

Реализуйте функцию, которая
- принимает очередь задач с указанием
    - времени их выполнения
    - и лимит.

Критерий отбора:
 - стараться оставить самые долгие задачи
 - но при этом максимально точно уложиться в лимит.


Данные:
tasks = {"task1": 5, "task2": 3, "task3": 7, "task4": 2}
time_limit = 10

Пример вывода:
time_limit = 10:
{'task3': 7, 'task2': 3}

time_limit = 12
{'task3': 7, 'task1': 5}

time_limit = 14
{'task3': 7, 'task1': 5, 'task4': 2}
"""

def filter_tasks_by_time(task_dict: dict[str, int], lim: int) -> dict[str, int]:
    if sum(task_dict.values()) > lim:
        sorted_tasks = sorted(task_dict.items(), key=lambda item: item[1], reverse=True)
        # print(sorted_tasks)
        total_time = 0
        res = {}

        for task_name, task_time in sorted_tasks:
            if total_time + task_time <= lim:
                res[task_name] = task_time
                total_time += task_time

        return res
    return task_dict




sample_10 = {'task3': 7, 'task2': 3}
sample_12 = {'task3': 7, 'task1': 5}
sample_14 = {'task3': 7, 'task1': 5, 'task4': 2}

tasks = {"task1": 5, "task2": 3, "task3": 7, "task4": 2}

result_10 = filter_tasks_by_time(tasks, 10)
print(result_10 == sample_10)

result_12 = filter_tasks_by_time(tasks, 12)
print(result_12 == sample_12)

result_14 = filter_tasks_by_time(tasks, 14)
print(result_14 == sample_14)