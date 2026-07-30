""" 04 Исключение при блокировке

Доработайте класс Door:
Создайте пользовательское исключение DoorBlockedError.
При попытке открыть дверь (или сменить код) во время блокировки
выбрасывайте это исключение вместо вывода сообщения.

Обработайте исключение в коде вызова.
"""

import time
from datetime import datetime, timedelta


class DoorBlockedError(Exception):
    """Raised when trying to access a blocked door."""


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
        if self.__is_blocked():
            raise DoorBlockedError(self.__remaining_block_time())

        if self.__is_valid_code(code):
            print("Access granted.")
        else:
            self.__handle_failed_attempt()
            print("Access denied.")

    def __handle_failed_attempt(self):
        self.__failed_attempts += 1
        self.__check_block()

    def __check_block(self):
        if self.__failed_attempts >= self.__max_attempts:
            self.__block_until = datetime.now() + self.__block_duration
            self.__remaining_block_time()
            print("Too many failed attempts.")

    def __remaining_block_time(self):
        remaining = self.__block_until - datetime.now()
        sec = int(remaining.total_seconds())
        return f"Door is blocked. Try again in {sec // 60} min {sec % 60} sec."


    def change_code(self, old_code, new_code):
        if self.__is_blocked():
            raise DoorBlockedError(self.__remaining_block_time())

        if self.__is_valid_code(old_code):
            self.__code = new_code
            print("Code changed.")
        else:
            print("Access denied. Code not changed.")
            self.__handle_failed_attempt()

    def __is_valid_code(self, code):
        return code == self.__code




if __name__ == "__main__":
    d = Door("1234", max_attempts=2, block_duration=0.05)

    try:
        d.unlock("1111")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')

    try:
        d.change_code("0000", "9999")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')

    try:
        d.unlock("1234")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')

    time.sleep(5)

    try:
        d.unlock("1234")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')


# Access denied.
# Access denied. Code not changed.
# Too many failed attempts.
# DoorBlockedError: Door is blocked. Try again in 0 min 2 sec.
# Access granted.