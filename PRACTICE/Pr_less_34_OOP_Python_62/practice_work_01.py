""" 01 Класс User

Создайте класс User, который описывает пользователя.

У каждого пользователя должно быть атрибуты экземпляра класса:
- username
- и email,
- а также счётчик входов login_count.

Добавьте метод show_info(), который выводит имя и почту пользователя.
Добавьте метод login(), который приветствует пользователя и фиксирует новый вход.
Добавьте метод get_logins(), возвращающий текущее количество входов.
Создайте пользователя, выполните несколько входов и выведите информацию.
Пример вывода:
------------------------------
Пользователь: alice
Почта: alice@example.com
------------------------------
alice вошёл в систему
alice вошёл в систему
Количество входов: 2

"""


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.login_count = 0

    def show_info(self):
            print("------------------------------")
            print(f"Пользователь: {self.username}")
            print(f"Почта: {self.email}")
            print("------------------------------")

    def login(self):
            self.login_count += 1
            print(f"{self.username} вошел в систему")

    def get_logins(self):
            return self.login_count



user1 = User("alice", "alice@example.com")

user1.show_info()
user1.login()
user1.login()

print(f"Количество входов: {user1.get_logins()}")

# ------------------------------
# Пользователь: alice
# Почта: alice@example.com
# ------------------------------
# alice вошёл в систему
# alice вошёл в систему
# Количество входов: 2