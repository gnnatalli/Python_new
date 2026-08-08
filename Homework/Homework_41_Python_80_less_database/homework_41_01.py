""" 01 Список всех стран

Используя базу данных world, вывести названия всех стран из таблицы country.
Каждое название должно отображаться с новой строки и иметь номер.
Пример вывода:
1. Aruba
2. Afghanistan
3. Angola
...
239. Zimbabwe

Попробуйте решить задачи используя стиль Data Access Object (DAO).
"""

import mysql.connector
from local_settings import dbconfig


class DatabaseError(Exception):
    """Общее исключение слоя доступа к данным"""


class MySQLConnection:
    pass


class WorldDB(MySQLConnection):
    def fetch_countries(self):
        """Получить список всех стран"""



if __name__ == "__main__":
    try:
        with WorldDB(dbconfig) as db:
            countries = db.fetch_countries()
            for i, name in enumerate(countries, start=1):
                print(f"{i}. {name}")
    except DatabaseError as e:
        print(f"❌ {e}")
