""" 01 Класс Door

Создайте класс Door, представляющий электронную дверь:
- при создании передаётся первоначальный код доступа (code)
- метод unlock(code):
    - разрешает доступ при правильном коде.
    - при неверном коде доступ отклоняется.

(Публичные, приватные или защищённые?)
Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми.
Пример вывода: 
Access denied.
Access granted.
"""

class Door:
    def __init__(self, code):
        self.__code = code

    def unlock(self, code):
        if self.__code == code:
            print("Access granted.")
        else:
            print("Access denied.")



if __name__ == "__main__":
    d = Door("1234")
    d.unlock("1234")
    d.unlock("0000")

# Access granted.
# Access denied.