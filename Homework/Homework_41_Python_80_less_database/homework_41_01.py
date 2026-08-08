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
    def __init__(self, config):
        self.config = config
        self.connection = None


    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            return self
        except mysql.connector.Error as err:
            raise DatabaseError(
                f"Ошибка подключения к базе данных: {err}"
            )


    def __exit__(self, exc_type, exc_val, traceback):
        if self.connection:
            self.connection.close()


class WorldDB(MySQLConnection):
    def fetch_countries(self):
        """Получить список всех стран"""

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                        SELECT Name
                        FROM country
                        ORDER BY Name
                        """
                )

                rows = cursor.fetchall()

            countries = []

            for row in rows:
                countries.append(row[0])

            return countries

        except mysql.connector.Error as e:
            raise DatabaseError(
                f"Ошибка получения списка стран: {e}"
            )


if __name__ == "__main__":
    try:
        with WorldDB(dbconfig) as db:
            countries = db.fetch_countries()
            for i, name in enumerate(countries, start=1):
                print(f"{i}. {name}")
    except DatabaseError as e:
        print(f"❌ {e}")
