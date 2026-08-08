""" 04 Фильтрация сотрудников по зарплате

Если в выбранном департаменте есть сотрудники — добавьте возможность отфильтровать их по зарплате.
Спросите пользователя:
Would you like to filter employees by salary? (y/n)
Если ответ — y, попросите ввести знак сравнения и значение:
Enter condition (>, <, =, >=, <=): >
Enter salary: 13000

Затем выведите только тех сотрудников, которые соответствуют критерию.
Если ответ — n, просто выведите всех сотрудников.

Пример вывода:
Enter department number: 8
You selected: Sales
Would you like to filter employees by salary? (y/n) y
Enter condition (>, <, =, >=, <=): >
Enter salary: 13000
1. John Russell — Sales Manager — 14000.00
2. Karen Partners — Sales Manager — 13500.00
"""

import mysql.connector
from local_settings import dbconfig

dbconfig['database'] = 'hr'

pass
