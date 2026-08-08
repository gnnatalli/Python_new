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


class DatabaseError(Exception):
    """Общее исключение слоя доступа к данным"""


class MySQLConnection:
    pass


class WorldDB(MySQLConnection):
    def fetch_countries(self):
        """Получить список всех стран"""


    def fetch_cities_by_country(self, country_name):
        """Получить все города выбранной страны с их населением"""


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
