""" 01 Список сотрудников по убыванию зарплаты

Доработайте код, который был на лекции (замените .close() на контекстный менеджер):
https://github.com/ibarbylev/logomashina/blob/master/IT_career_hub/PD_Python/less_41__database/theory_03__mysql-connector-python.py

Выведите список департаментов в формате:
№ Название департамента.

Добавьте возможность вывода списка сотрудников по имени департамента.

Добавьте сортировку сотрудников выбранного департамента по убыванию зарплаты.
Выведите имя, фамилию, должность и зарплату каждого сотрудника, начиная с самого высокооплачиваемого.
Также добавьте нумерацию (не id).

Пример вывода:
Enter department: Marketing
1. Michael Hartstein — Marketing Manager — 13000.00
2. Pat Fay — Marketing Representative — 6000.00
Решение:
"""

"""
Пример использования библиотеки mysql-connector-python

Установка: pip install mysql-connector-python

Возможны проблемы с установкой на Windows.
Рекомендация: "откатить" более старую версию пакета, например:

pip uninstall mysql-connector-python
pip install mysql-connector-python==9.3.0

Если не поможет - следует "опуститься" ещё "ниже".
"""

import mysql.connector
from local_settings import dbconfig

dbconfig["database"] = "hr"

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT department_id, department_name
            FROM departments
            ORDER BY department_id
            """
        )

        departments = cursor.fetchall()


        for number, department in departments:
            print(f"{number}. {department}")

        dep_name = input(
            "Введите имя департамента: "
        )

        cursor.execute(
            """
            SELECT
                e.first_name,
                e.last_name,
                j.job_title,
                e.salary,
                d.department_name
            FROM employees AS e
            JOIN jobs AS j USING (job_id)
            JOIN departments AS d USING (department_id)
            WHERE d.department_name = %s
            ORDER BY e.salary DESC
            """,
            (dep_name,))

        for i, r in enumerate(cursor.fetchall(), start=1):
            print(f"{i}. {r[0]} {r[1]} — {r[2]} — {r[3]}")


