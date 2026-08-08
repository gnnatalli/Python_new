""" 01 Создание базы

Напишите программу, которая:
- создаёт базу данных notes_app_<your_group>_<your_full_name>
- выбирает эту базу через USE notes_app
- выводит сообщение о результате

Пример вывода:
Database 'notes_app' created or already exists.
"""

import mysql.connector
from local_settings import dbconfig_write

db_name = ...

pass


# Database 'notes_app_112226_abcdefg' created or already exists.
