""" 02 Города выбранной страны

Добавьте к предыдущей программе возможность выбора страны.
Пользователь должен ввести название страны.
Далее выведите все города этой страны и их численность населения.

Пример вывода 1:
Введите страну: Germany
Berlin — 3386667
Hamburg — 1704735
Munich [München] — 1194560

Пример вывода 2:
Введите страну: Unknown
❌ Страна 'Unknown' не найдена
...

"""

import mysql.connector
from local_settings import dbconfig

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
                cursor.execute(
                    """
                    SELECT Name
                    FROM world.country
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


    def fetch_cities_by_country(self, country_name):
        """Получить все города выбранной страны с их населением"""

        try:
            with self.connection.cursor(dictionary=True) as cursor:

                # Сначала ищем страну и получаем её код
                cursor.execute(
                    """
                    SELECT Code
                    FROM world.country
                    WHERE Name = %s
                    """,
                    (country_name,)
                )

                country = cursor.fetchone()

                # Если такой страны нет
                if country is None:
                    return None

                country_code = country["Code"]

                # Теперь ищем города по коду страны
                cursor.execute(
                    """
                    SELECT Name, District, Population
                    FROM world.city
                    WHERE CountryCode = %s
                    ORDER BY Population DESC
                    """,
                    (country_code,)
                )

                cities = cursor.fetchall()

                return cities

        except mysql.connector.Error as e:
            raise DatabaseError(
                f"Ошибка получения списка городов: {e}"
            )


if __name__ == "__main__":
    try:
        with WorldDB(dbconfig) as db:
            # Список всех стран
            countries = db.fetch_countries()
            print("Список стран:")
            for i, name in enumerate(countries, start=1):
                print(f"{i}. {name}")

            # Ввод страны пользователем
            country_input = input("\nВведите страну: ").strip()

            # Получаем города выбранной страны
            cities = db.fetch_cities_by_country(country_input)
            if not cities:
                print(f"Для страны '{country_input}' нет данных о городах.")
            else:
                for city in cities:
                    # Формируем строку с названием города и населением
                    city_name = city['Name']
                    district = city['District']
                    population = city['Population']
                    # Если нужно — можно добавить район/альтернативное имя
                    print(f"{city_name} — {population}")

    except DatabaseError as e:
        print(f"❌ {e}")
