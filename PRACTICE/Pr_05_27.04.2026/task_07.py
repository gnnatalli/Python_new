""" 07 Кодирование строки

Напишите программу, которая
- принимает строку
- и кодирует её с помощью следующего правила:
    - каждая последовательность одинаковых символов заменяется на:
        - символ
        - и количество его повторений.

Например, строка aaaabbc превращается в a4b2c1.

Пример вывода:
Исходная строка: aaaabbc
Закодированная строка: a4b2c1
"""


text = "aaaabbc"
print("Исходная строка:", text)

count = 1
encoded_text = ""

for i in range(1, len(text)):
    if text[i] == text[i-1]:
        count += 1
    else:
        encoded_text += text[i-1] + str(count)
        count = 1

encoded_text += text[i] +str(count)

print("Закодированная строка:", encoded_text)