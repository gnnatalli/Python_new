""" 03 Пустой департамент
Добавьте в программу проверку: если в выбранном департаменте нет сотрудников, вместо списка сотрудников выведите сообщение:
No employees found in this department.
Пример вывода:
Enter department number: 27
You selected: Payroll
No employees found in Payroll department.
"""
""" 03 Пустой департамент
Добавьте в программу проверку: если в выбранном департаменте нет сотрудников, вместо списка сотрудников
выведите сообщение:
No employees found in this department.
Пример вывода:
Enter department number: 27
You selected: Payroll
No employees found in Payroll department.
"""

from pprint import pprint

import mysql.connector
from local_settings import dbconfig

dbconfig['database'] = 'hr'

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:

        cursor.execute("SELECT department_id, department_name FROM departments ORDER BY department_id")
        departments = cursor.fetchall()

        for number, department in departments:
            print(f"{number}. {department}")

        dep_id = input("Введите номер Департамента: ")
        cursor.execute(
            "SELECT department_name FROM departments WHERE department_id = %s",
            (dep_id, )
        )
        print(f"You choose: {cursor.fetchone()[0]} ")

        cursor.execute(""" SELECT 
            e.first_name, e.last_name, j.job_title, e.salary, d.department_name
            FROM 
            employees AS e
                JOIN
            jobs AS j USING(job_id)
                JOIN
            departments AS d USING(department_id)
            WHERE
                d.department_id = %s
            ORDER BY
                e.salary DESC
                """, (dep_id,))

        employees = cursor.fetchall()
        if employees:
            for i, r in enumerate(employees, start=1):
                print(f"{i}. {r[0]} {r[1]} — {r[2]} — {r[3]}")
        else:
            print("No employees found in this department.")