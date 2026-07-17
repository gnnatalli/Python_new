""" 01 Генерация безопасных паролей
Программа должна сгенерировать все возможные пароли длиной 4 символа, соблюдая следующие условия:
- Пароль должен содержать хотя бы одну заглавную букву, одну строчную букву и одну цифру.
- Символы не должны повторяться.
- Соседние символы не могут быть расположены подряд в таблице символов.
- Все подходящие пароли записываются в файл valid_passwords.txt в формате:
   1: ACa0
   2: ACa1
   3: ACa2
   4: ACa3

Подсказки:

1. Можно сначала получить все возможные варианты,
а затем оставить из них только те, что удовлетворяют условиям валидации.

2. Общее число всех возможных комбинаций (и валидных, и нет) более 13 миллионов.
Поэтому держать их все в памяти одновременно - КРАЙНЕ расточительно.
"""




# from itertools import product
# import string
#
# # Все допустимые символы
# symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
#
#
# def is_valid(password):
#     # Есть хотя бы одна заглавная буква
#     has_upper = any(ch.isupper() for ch in password)
#
#     # Есть хотя бы одна строчная буква
#     has_lower = any(ch.islower() for ch in password)
#
#     # Есть хотя бы одна цифра
#     has_digit = any(ch.isdigit() for ch in password)
#
#     # Символы не повторяются
#     if len(set(password)) != len(password):
#         return False
#
#     # Соседние символы не идут подряд в таблице символов
#     indexes = [symbols.index(ch) for ch in password]
#
#     for i in range(len(indexes) - 1):
#         if abs(indexes[i] - indexes[i + 1]) == 1:
#             return False
#
#     return has_upper and has_lower and has_digit
#
#
# counter = 1
#
# with open("valid_passwords.txt", "w") as file:
#     for password in product(symbols, repeat=4):
#         password = "".join(password)
#
#         if is_valid(password):
#             file.write(f"{counter}: {password}\n")
#             counter += 1
#
# print(f"Найдено {counter - 1} подходящих паролей.")



# Вариант Димы
# import itertools
# import string
#
#
# PASSWORD_LENGTH = 4
# OUTPUT_FILE = "valid_passwords.txt"
# CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits
#
#
# def has_required_symbols(password):
#     return (
#         any(symbol.isupper() for symbol in password)
#         and any(symbol.islower() for symbol in password)
#         and any(symbol.isdigit() for symbol in password)
#     )
#
#
# def has_no_neighboring_ascii_symbols(password):
#     return all(
#         abs(ord(current_symbol) - ord(next_symbol)) != 1
#         for current_symbol, next_symbol in zip(password, password[1:])
#     )
#
#
# def is_valid_password(password):
#     return (
#         has_required_symbols(password)
#         and has_no_neighboring_ascii_symbols(password)
#     )
#
#
# def generate_valid_passwords():
#     for password_symbols in itertools.permutations(CHARS, PASSWORD_LENGTH):
#         password = "".join(password_symbols)
#
#         if is_valid_password(password):
#             yield password
#
#
# def main():
#     with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
#         for number, password in enumerate(generate_valid_passwords(), start=1):
#             file.write(f"{number}: {password}\n")
#
#
# if __name__ == "__main__":
#     main()

# Вариант Ильи
from itertools import permutations

UPPERS = "".join(map(chr, range(ord('A'), ord('Z')+1)))
LOWERS = "".join(map(chr, range(ord('a'), ord('z')+1)))
DIGITS = "".join(map(chr, range(ord('0'), ord('9')+1)))
WORD = UPPERS + LOWERS + DIGITS

def is_valid(pwd):
    return all([
        any(char in UPPERS for char in pwd),
        any(char in LOWERS for char in pwd),
        any(char in DIGITS for char in pwd),
        all(abs(ord(pwd[i]) - ord(pwd[i+1])) > 1 for i in range(len(pwd) - 1))
    ])

with open('valid_passwords.txt', 'w', encoding='utf-8') as f:
    row = 1
    for password in permutations(WORD, 4):
        if is_valid(password):
            f.write(f'{row:7}: {"".join(password)}\n')
            row += 1
