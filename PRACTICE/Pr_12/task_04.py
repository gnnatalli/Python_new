""" 04 Сумма продаж

Есть дерево подразделений внутри компании
(каждое подразделение может содержать «дочерние» отделы).
Напишите рекурсивную функцию, которая
- подсчитывает суммарные продажи для всех отделов.

Функция должна проверять:
- Аргумент должен быть словарем.
- Дочерние отделы (если есть) должны быть списком словарей.

Если данные не валидны необходимо выбрасывать исключение.
При вызове функции обработайте возможное исключение.

Данные:
company_structure = {
    "dept_name": "Head Office",
    "sales": 100,
    "sub_departments": [
        {
            "dept_name": "Sales Department",
            "sales": 200,
            "sub_departments": [
                {
                    "dept_name": "B2B Sales",
                    "sales": 120,
                }
            ]
        },
        {
            "dept_name": "IT Department",
            "sales": 150,
            "sub_departments": [
                {
                    "dept_name": "DevOps",
                    "sales": 300,
                    "sub_departments": [
                        {
                            "dept_name": "Cloud Infrastructure",
                            "sales": 180,
                        }
                    ]
                },
                {
                    "dept_name": "QA Department",
                    "sales": 90,
                }
            ]
        }
    ]
}

Пример вывода:
Общая сумма продаж: 1140
"""

company_structure = {
    "dept_name": "Head Office",
    "sales": 100,
    "sub_departments": [
        {
            "dept_name": "Sales Department",
            "sales": 200,
            "sub_departments": [
                {
                    "dept_name": "B2B Sales",
                    "sales": 120,
                }
            ]
        },
        {
            "dept_name": "IT Department",
            "sales": 150,
            "sub_departments": [
                {
                    "dept_name": "DevOps",
                    "sales": 300,
                    "sub_departments": [
                        {
                            "dept_name": "Cloud Infrastructure",
                            "sales": 180,
                        }
                    ]
                },
                {
                    "dept_name": "QA Department",
                    "sales": 90,
                }
            ]
        }
    ]
}

def summarize_sales(department, sales_name):
    pass

try:
    pass
except ...:
    pass