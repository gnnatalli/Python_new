""" 08 Проверка формата email

Напишите программу, которая проверяет
- начинается ли строка с буквы,
- содержит ли в себе символ @,
- и заканчивается ли на .com или .de.

Пример вывода:
email: user@example.com
Корректный формат? True
"""
from operator import is_

email = "user@example.com"

is_email = (email[0].isalpha()
            and "@" in email
            and (email.endswith(".com") or email.endswith(".de")))

print("email: ", email)
print("Корректный формат? ", is_email)
