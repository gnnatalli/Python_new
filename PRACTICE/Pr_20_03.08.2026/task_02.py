""" 02 Выбор департамента по номеру

Модифицируйте предыдущую программу так, чтобы пользователь выбирал департамент по номеру из списка,
а не вручную вводил его название.
После выбора выведите название департамента и продолжите выполнение.

Пример вывода:
Enter department number: 2
You choose: Marketing
1. Michael Hartstein — Marketing Manager — 13000.00
2. Pat Fay — Marketing Representative — 6000.00
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

