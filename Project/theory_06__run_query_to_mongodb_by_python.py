from pprint import pprint
from pymongo import MongoClient  # pip install pymongo

from local_settings import MONGODB_URL_READ

with MongoClient(MONGODB_URL_READ) as client:
    TIMES = 5  # число документов на печать по умолчанию
    task_statement = []  # список условий задач
    data = []  # список документов по каждому решению задачи

    """ ********************** Блок задач **************************** """

    # === Задача 1 (пример решения) ===
    task_statement.append(
        ' 1. Из коллекции customers выяснить из какого города "Sven Ottlieb"'
    )

    # ----- в result подставляем решение из mongodb -----
    filter = {
        'ContactName': 'Sven Ottlieb'
    }
    project = {
        'City': 1,
        '_id': 0
    }
    limit = 1

    result = client['ich']['customers'].find(
        filter=filter,
        projection=project,
        limit=limit
    )

    data.append(result)

    # ===== Задача 2 =====
    task_statement.append(
        '2. Из коллекции ich.US_Adult_Income найти возраст самого взрослого человека'
    )

    # ----- в result подставляем решение из mongodb -----

    filter = {}
    sort = list({
                    'age': -1
                }.items())
    limit = 1

    result = client['ich']['US_Adult_Income'].find(
        filter=filter,
        sort=sort,
        limit=limit
    )

    data.append(result)

    # ===== Задача 3 =====
    task_statement.append(
        '3. Из 2 задачи выясните, сколько человек имеют такой же возраст'
    )

    # ----- в result подставляем решение из mongodb -----

    filter = {
        'age': 90
    }
    project = {
        'age': 1,
        '_id': 0
    }
    sort = list({
                    'age': -1
                }.items())

    result = client['ich']['US_Adult_Income'].find(
        filter=filter,
        projection=project,
        sort=sort
    )

    data.append(result)

    # ===== Задача 4 =====
    task_statement.append(
        '4. Найти _id ObjectId документа, в котором education " IT-career-hub"'
    )
    # ----- в result подставляем решение из mongodb -----

    filter = {
        'education': ' IT-career-hub'
    }
    project = {
        'education': 1
    }

    result = client['ich']['US_Adult_Income'].find(
        filter=filter,
        projection=project
    )

    data.append(result)

    # ===== Задача 5 =====
    task_statement.append(
        '5. Выяснить количество людей в возрасте между 20 и 30 годами'
    )

    # ----- в result подставляем решение из mongodb -----

    filter = {
        'age': {
            '$gt': 20,
            '$lt': 30
        }
    }
    project = {
        'age': 1,
        '_id': 0
    }

    result = client['ich']['US_Adult_Income'].find(
        filter=filter,
        projection=project
    )
    data.append(result)

    """ *************** Блок вывода всех результатов на печать *************** """

    if len(data) != len(task_statement):
        raise IndexError("Ошибка!!! Кол-во заданий НЕ РАВНО кол-ву решений!!!")

    # Цикл по задачам
    for task_num, result in enumerate(data):
        print(50 * '=')
        print(task_statement[task_num])
        print()

        # Цикл по выводу документов решения
        docs = list(result)
        for idx, doc in enumerate(docs[:TIMES]):
            # print(idx, 50 * '-')
            pprint(doc)

        print(f"Total: {len(docs)} docs")