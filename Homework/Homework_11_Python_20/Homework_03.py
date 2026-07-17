# Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент,
# умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."

result = ""
number = ""

for ch in text:
    if ch.isdigit() or ch == ".":
        number = number + ch
    else:
        if number != "":
                result = result + str(float(number) * 10)
    number = ""
    result = result + ch

# если число в конце строки
if number != "":
    result = result + str(float(number) * 10)

print(result)