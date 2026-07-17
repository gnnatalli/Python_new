'''1. Фильтрация по ключевому слову

Напишите программу, которая ищет в файле все строки, содержащие указанное пользователем слово, и сохраняет их в новый файл.

Имя нового файла формируется как <keyword>_<original_filename>.

Если файл не существует, программа должна вывести ошибку.

Если совпадения не найдены, новый файл не создаётся.

Используйте файл system_log.txt.

Пример ввода:

Введите имя файла для поиска: system_log.txt

Введите ключевое слово: error

Пример вывода:

Строки, содержащие 'error', сохранены в error_system_log.txt.'''

try:
#     Вводим данные
    filename = input("Введите имя файла для поиска: ")
    keyword = input("Введите ключевое слово: ")

#   Читаем исходный файл
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

#     Ищем строки с ключевым словом
    found_lines = []

    for line in lines:
        if keyword in line:
            found_lines.append(line)

#     Если совпадения есть - создаем новый файл
    if found_lines:
        new_filename = f"{keyword}_{filename}"

        with open(new_filename, "w", encoding="utf-8") as new_file:
            new_file.writelines(found_lines)

        print(f"Строки содержащие '{keyword}', сохранены в {new_filename}.")
    else:
        print(f"Строки содержащие '{keyword}' не найдены.")

except FileNotFoundError:
    print("Ошибка: файл не существует.")