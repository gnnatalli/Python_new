""" 05 Читабельный формат словаря

Дан вложенный словарь. Напишите рекурсивную функцию, которая
- преобразует его в «плоский» формат,
    где в ключе будет содержаться полный путь к значению.

Данные:
data = {
    "user": {
        "id": 123,
        "info": {
            "name": "Alice",
            "location": {
                "city": "Berlin",
                "coordinates": {"lat": 52.52, "lon": 13.405}
            },
            "hobby": ["swimming", "drawing"]
        }
    },
    "score": 95
}

Пример вывода:
Данные для анализа:
user.id : 123
user.info.name : Alice
user.info.location.city : Berlin
user.info.location.coordinates.lat : 52.52
user.info.location.coordinates.lon : 13.405
user.info.hobby : ['swimming', 'drawing']
score : 95
"""


def parse_data(data, parent_key="", result=None):
    pass


data = {
    "user": {
        "id": 123,
        "info": {
            "name": "Alice",
            "location": {
                "city": "Berlin",
                "coordinates": {"lat": 52.52, "lon": 13.405}
            },
            "hobby": ["swimming", "drawing"]
        }
    },
    "score": 95
}

parsed_data = parse_data(data)
print("Данные для анализа:")
for k, v in parsed_data.items():
    print(k, ":", v)