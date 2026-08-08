""" 3.2. Регистрация клиента

Добавьте в основное меню пункт, который позволяет пользователю зарегистрироваться в системе.
Пользователь вводит логин, пароль и стартовый баланс;
Логин должен быть уникальным — если такой пользователь уже существует,
регистрация отклоняется "Username already exists.";

Если регистрация прошла успешно — выведите сообщение Registration successful.

Если логин занят — выведите Username already exists.

Пример ввода:
Enter username: alice
Enter password: qwerty
Enter initial balance: 150
Пример вывода:
Registration successful.
"""
import mysql.connector


def register_user(connection, db_name):
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        balance = float(input("Enter initial balance: "))
    except ValueError:
        print("Invalid balance.")
        return

    if balance < 0:
        print("Invalid balance.")
        return

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"USE `{db_name}`")

            # Проверка: логин занят?
            cursor.execute(
                """
                SELECT id
                FROM users
                WHERE username = %s
                """,
                (username,)
            )

            user = cursor.fetchone()

            if user is not None:
                print("Username already exists.")
                return

            # Добавляем нового пользователя
            cursor.execute(
                """
                INSERT INTO users (username, password, balance)
                VALUES (%s, %s, %s)
                """,
                (username, password, balance)
            )

        connection.commit()
        print("Registration successful.")

    except mysql.connector.Error as error:
        connection.rollback()
        print(f"Database error: {error}")




# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.
# 2
# 2. Register new user
# Enter username: alex
# Enter password: 123
# Enter initial balance: 100
# Registration successful.
#
# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.
