""" 06 Числа и слова

Напишите программу, которая
- обрабатывает строку, содержащую слова и целые числа, разделённые пробелами.

Программа должна преобразовать строку в список, где
- числа преобразуются в тип int,
- а остальные элементы остаются строками и начинаются с заглавной буквы.

text = "apple 42 banana 3 100 orange"

Пример вывода:
Изначальная строка: apple 42 banana 3 100 orange
Результат: ['Apple', 42, 'Banana', 3, 100, 'Orange']
"""

text = "apple 42 banana 3 100 orange"

text_parts = text.split()

out_text = []

for item in text_parts:
    if item.isdigit() :

       out_text += [int(item)]
    else:
        out_text += [item.title()]

print("Изначальная строка:", text)
print("Результат:", out_text)


