"""01 Список файлов и папок

Напишите программу, которая
- принимает путь к директории через аргумент командной строки
- и выводит:
    - Отдельно список папок
    - Отдельно список файлов

Пример запуска:
python script.py /home/user/documents

Пример вывода:
Содержимое директории '/home/user/documents':
Папки:
- folder1
- folder2
Файлы:
- file1.txt
- file2.txt
- notes.docx
"""

import os
import sys

def list_directory_contents(dir_path):
    # Проверяем, существует ли указанный путь и является ли он директорией
    if not(os.path.exists(dir_path)):
        print(f"Ошибка: Путь '{dir_path}' не существует.")
        return
    if not(os.path.isdir(dir_path)):
        print(f"Ошибка: Путь '{dir_path}' не является директорией.")
        return

    try:
        # Получаем список всех элементов и директорий
        all_items = os.listdir(dir_path)
    except PermissionError:
        print(f"Ошибка: Нет доступа к директории '{dir_path}'.")
        return

    folders = []
    files = []

    # Разделяем элементы на файлы и папки
    for item in all_items:
        # Собираем полный путь к элементу для корректной проверки
        full_path = os.path.join(dir_path, item)

        if os.path.isdir(full_path):
            folders.append(item)
        elif os.path.isfile(full_path):
            files.append(item)

        # Выводим результат
        print(f"Содержимое директории '{dir_path}': ")

        print("Папки: ")
        if folders:
            for folder in sorted(folders):
                print(f'- {folder}')
        else:
            print(" (нет папок)")

        print("Файлы: ")
        if files:
            for file in sorted(files):
                print(f'- {file}')
        else:
            print(" (нет файлов)")

if __name__ == "__main__":
    # Проверяем передан ли аргумент командной строки
    if len(sys.argv) < 2:
       print("Использование: python script.py '/home/Users/ICH/ICH_KURS'")
       sys.exit(1)

#     Первый аргумент (sys.argv[1]) - это путь, переданный пользователем
    target_path = sys.argv[1]
    list_directory_contents(target_path)

