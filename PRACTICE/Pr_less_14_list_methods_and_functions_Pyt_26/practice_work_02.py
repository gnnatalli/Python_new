""" 02 Слова, начинающиеся с гласных

Напишите программу, которая
- обрабатывает список строки
- создает новый список, где строки, начинающиеся с гласной буквы
        будут заканчиваться символом "!".
- Остальные слова добавьте в том же виде.

Дополнительно:
EN_VOWELS = "aeiouyAEIOUY"
RU_VOWELS = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

Данные:
strings = ["apple", "banana", "cherry", "grape", "orange"]

Пример вывода:
Результат: ['apple!', 'banana', 'cherry', 'grape', 'orange!']

"""
EN_VOWELS = "aeiouyAEIOUY"
RU_VOWELS = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

strings = ["apple", "banana", "cherry", "grape", "orange"]
new_strings = []