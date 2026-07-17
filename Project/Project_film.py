"""
Пакет mysql.connector внешней, поэтому требует предварительной инсталляции:

pip install mysql-connector-python

Кроме того, требуется сохранить в отдельном файле local_settings.py параметры подключения
"""

import mysql.connector
from tabulate import tabulate  # pip install tabulate
from local_settings import dbconfig

connection = mysql.connector.connect(**dbconfig)

cursor = connection.cursor()

q_get_by_name="""
    SELECT title, description, release_year
    FROM film
    WHERE title LIKE %s
    LIMIT 10 OFFSET %s; 
"""

q_get_by_genres_and_years = """
    SELECT title, description, release_year, category_id
    FROM film as f
    JOIN film_category fc USING (film_id)
    WHERE category_id = %s
    AND release_year BETWEEN %s AND %s;
"""


# print("Список жанров из БД sakila:")
# page = 1
# cursor.execute(q_get_by_name, ('%a%', (page-1)*10))
# rows = cursor.fetchall()
#
# headers = [col[0] for col in cursor.description]
#
# print(tabulate(rows, headers=headers, tablefmt="psql"))

print("Список жанрам и годам из БД sakila:")
page = 1
cursor.execute(q_get_by_genres_and_years, (1, 1994, 2003))
rows = cursor.fetchall()

headers = [col[0] for col in cursor.description]

print(tabulate(rows, headers=headers, tablefmt="psql"))