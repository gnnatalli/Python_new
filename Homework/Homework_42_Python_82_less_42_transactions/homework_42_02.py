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

db_name = ...

pass

# Database 'notes_app_112226_abcdefg' created or already exists.
#
# All notes:
# {'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}
#
# Process finished with exit code 0
