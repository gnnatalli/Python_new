""" 03 Блокировка двери

Доработайте класс Door:
- при создании можно указать:
    - максимальное количество попыток (по умолчанию 3)
    - время блокировки в минутах (по умолчанию 15)
- если попытки исчерпаны, дверь блокируется на указанное время.
- пока дверь заблокирована — сменить код или открыть нельзя.
- неверные попытки входа (или смены кода) учитываются общим счётчиком.
- при блокировке должно выводиться сообщение с указанием оставшегося времени ожидания.
"""

import time
from datetime import datetime, timedelta

class Door:

    def __init__(self, code, max_attempts = 3, block_duration = 15):
        self.__code = code
        self.__failed_attempts = 0
        self.__max_attempts = max_attempts
        self.__block_duration: timedelta = timedelta(minutes=block_duration)
        self.__block_until = None

    def __is_blocked(self):
        return self.__block_until is not None and datetime.now() < self.__block_until

    def unlock(self, code):
        if self.__is_valid_code(code) and not self.__is_blocked():
            print("Access granted.")
        else:
            print("Access denied.")
            self.__handle_failed_attempt()

    def __handle_failed_attempt(self):
        self.__failed_attempts += 1
        self.__check_block()

    def __check_block(self):
        if self.__failed_attempts >= self.__max_attempts:
            self.__block_until = datetime.now() + self.__block_duration
            print("Too many failed attempts.")
            self.__remaining_block_time()

    def __remaining_block_time(self):
        remaining = self.__block_until - datetime.now()
        sec = int(remaining.total_seconds())
        print(f"DoorBlockedError: Door is blocked. Try again in {sec // 60} min {sec % 60} sec.")


    def change_code(self, old_code, new_code):
        if self.__is_valid_code(old_code):
            self.__code = new_code
            print("Code changed.")
        else:
            print("Access denied. Code not changed.")
            self.__handle_failed_attempt()

    def __is_valid_code(self, code):
        return code == self.__code


# Пример использования
d = Door("1234", max_attempts=2, block_duration=0.05)

d.unlock("1111")
d.change_code("2222", "9999")
d.unlock("1234")
time.sleep(5)
d.unlock("1234")

