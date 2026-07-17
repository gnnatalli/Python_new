# Звёздочки вместо чисел
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
# text = "My number is 123-456-789"
# Пример вывода:
# Строка: My number is 123-456-789
# Результат: My number is ***-***-***

text = "My number is 123-456-789"
result = ""

for ch in text:
    if ch.isdigit():
        result = result + "*"
    else:
        result = result + ch

print("Строка: ", text)
print("Результат: ", result)