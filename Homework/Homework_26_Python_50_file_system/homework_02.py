""" 02 Поиск и удаление файлов с указанным расширением

Напишите программу, которая
- Принимает путь к директории и расширение файлов через аргумент командной строки.
- Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
- Спрашивает у пользователя, хочет ли он удалить найденные файлы.
- Если пользователь подтверждает, удаляет их.

Пример запуска
python script.py /home/user/PycharmProjects/project1 .log

Пример вывода:
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log

Вы хотите удалить эти файлы? (y/n): y
Удаление завершено.
"""

import os
import sys


def find_files_with_extension(directory, extension):
    """Рекурсивно ищет файлы с заданным расширением."""
    found_files = []

#     os.walk возвращает кортеж: (текущий_путь, список_подпапок, список_файлов)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
#                 Объединяем путь к папке и имя файла
                full_path = os.path.join(root, file)
                found_files.append(full_path)

    return found_files

# Предварительно создаём ненужные файлы для удаления
files = [
    'error.log',
    'system.log',
    'old.log',
    'debug.log',
]

for file in files:
    with open(file, 'w') as f:
        f.write("")

# Проверяем количество аргументов
if len(sys.argv) !=3:
    print("Использование: ")
    print(f"python {sys.argv[0]} /home/Users/PycharmProjects/project1 .log")
    sys.exit(1)

directory = sys.argv[1]
extension = sys.argv[2]

# Проверяем существование директории
if not os.path.isdir(directory):
    print("Ошибка: указанная директория не существует.")
    sys.exit(1)

found_files = find_files_with_extension(directory, extension)

if not found_files:
    print(f"Файлы с расширением '{extension}' не найдены.")
    sys.exit()

print(f"Найдены файлы с расширением '{extension}': ")
for file in found_files:
    print("-", file)

answer = input("\n Вы хотите удалить этот файл? (y/n): ")

if answer.lower() == "y":
    for file in found_files:
        os.remove(file)
    print("Удаление завершенно.")
else:
    print("Удаление отмененно.")