""" 02 Добавление заметок

Продолжите предыдущую программу:
- создайте таблицу notes с полями: id, title, content
- вставьте одну заметку в таблицу
- выполните commit() после вставки
- выведите все заметки используя в формате dict (а не tuple!)

Пример вывода:

All notes:
{'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}

"""

import mysql.connector
from local_settings import dbconfig_write

db_name = "notes_app_060326_ptm_Nataliia_Honchar"

with mysql.connector.connect(**dbconfig_write) as connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {db_name}"
        )

        cursor.execute(
            f"USE {db_name}"
        )

        print(
            f"Database {db_name} created or already exists."
        )

        # Создаём таблицу notes

        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS notes
            (
                id
                INT
                AUTO_INCREMENT
                PRIMARY
                KEY,
                title
                VARCHAR
            (
                255
            ),
                content text
                )
        """
            )

        # Добавляем одну заметку
        cursor.execute(
            """ 
            INSERT INTO notes (title, content)
            VALUES (%s, %s) 
            """,
            (
                "First Note",
                "This is the content of my first note."
            )
        )
        # Сохраняем INSERT
        connection.commit()

    # Новый cursor, который возвращает dict
    with connection.cursor(dictionary=True) as cursor:

        cursor.execute(
            """
            SELECT id, title, content 
            FROM notes
            """
        )

        notes = cursor.fetchall()

        print("\n All notes:")

        for note in notes:
            print(note)

# Database 'notes_app_112226_abcdefg' created or already exists.
#
# All notes:
# {'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}
#
# Process finished with exit code 0
