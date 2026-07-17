'''2.Поиск и удаление дубликатов

Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.

Имя нового файла формируется как unique_<original_filename>.

Если файл не существует, программа должна вывести ошибку.

Исходный порядок строк должен сохраниться.

Если в файле нет дубликатов, создаётся точная копия файла.

Используйте файл movies_to_watch.txt.

Пример ввода:

Введите имя файла: movies_to_watch.txt

Пример вывода:

Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.'''


try:
#     Вводим имя файла
    filename = input("Введите имя файла: ")

#     Читаем файл
    with open(filename, "r", encoding="utf=8") as file:
        lines = file.readlines()

#     Удаляем дубликаты, сохраняя порядок
    unique_lines = []
    seen = set()

    for line in lines:
        if line not in seen:
            unique_lines.append(line)
            seen.add(line)

#     Создаем новый файл
    new_filename = f"unique_{filename}"

    with open(new_filename, "w", encoding="utf-8") as new_file:
        new_file.writelines(unique_lines)

    print(f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}. ")

except FileNotFoundError:
    print("Ошибка: файл не существует.")

