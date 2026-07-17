""" 01. Одно слово

Напишите программу, которая
- обрабатывает список из строк
- и удаляет все строки, содержащие более одного слова,
- а также преобразует оставшиеся строки к нижнему регистру.

ВАЖНО: НЕ создать новый список, а УДАЛИТЬ лишние элементы из существующего!

Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
"""

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

i = 0

while i < len(text_list):
    if len(text_list[i].split()) > 1:
        del text_list[i]
    else:
        text_list[i] = text_list[i].lower()
        i += 1

print("Обработанный список: ", text_list)