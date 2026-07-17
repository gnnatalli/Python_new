""" Решение выполняем в PyCharm (Jupyter Notebook или Colab)

С помощью pandas создайте таблицу с данными о погоде в вашем городе
за последние 7 дней. Таблица должна включать следующие столбцы:

- Дата
- Температура днем
- Температура ночью
- Продолжительность светового дня
- Скорость ветра
- Влажность
- Атмосферное давление

Данные могут быть любыми, но в пределах норм. """

import pandas as pd
import sqlite3
from tabulate import tabulate

# Создаём словарь с данными

data = {
    "Date": ["2026-06-18", "2026-06-19", "2026-06-20", "2026-06-21", "2026-06-22", "2026-06-23", "2026-06-24"],
    "Day temperature": [28, 30, 31, 27, 25, 24, 26],
    "Night temperature": [10, 11, 12, 13, 14, 15, 16],
    "Daylight": [11, 12.2, 13.1, 14.2, 15.1, 16.1, 11],
    "Wind speed": [12, 14, 15, 16, 17, 18, 5],
    "Humidity": [65, 80, 50, 62, 48, 50, 70],
    "Pressure": [750, 720, 700, 800, 900, 755, 810]
 }

# pd.set_option('display.max_columns', None) # показать все столбцы
# Преобразуем словарь в DataFrame
df = pd.DataFrame(data)

# Выводим таблицу
print(df)



# Преобразуем словарь в DataFrame

# 1. Создаём подключение к СУБД SQLite
conn = sqlite3.connect('weather.db')

# 2. `pandas` содержит встроенный метод `to_sql`, благодаря чему
df.to_sql(
    'new_weather',   # имя таблицы в БД
    conn,          # подключение к базе
    if_exists='replace',  # заменить таблицу, если она уже существует
    index=False    # не сохранять индекс pandas как отдельный столбец
)

# Выполняем SQL-запрос и сразу получаем DataFrame
df_from_db = pd.read_sql_query(
    'SELECT * FROM new_weather',
    conn
)
 conn.close()
# Вывод результата
# print(df_from_db)

print(tabulate (df_from_db, headers='keys', tablefmt='psql', showindex=False))
