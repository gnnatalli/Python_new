""" 3.3. Вход в аккаунт

Добавьте в меню пункт, который позволяет пользователю войти в свой аккаунт.
Пользователь вводит логин и пароль;
Если данные корректны — вход считается успешным, и запускается новое подменю клиента;
Если данные неверны — выведите сообщение Invalid username or password.
После входа в систему переменная user_id сохраняется,
и пользователь попадает в дополнительное меню.

Выход из дополнительного возвращает обратно в главное меню.

Пример ввода:
Enter username: alice
Enter password: qwerty

Пример вывода:
Login successful.
"""
import mysql.connector

from queries import text_user_menu

def try_login(connection, db_name):
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"USE {db_name}")

            cursor.execute("""
                SELECT id
                FROM users
                WHERE username = %s AND password = %s
                """,
                (username, password)
            )

            user = cursor.fetchone()


    # Если пользователь найден - возвращаем его user_id
            if user is not None:
                print("Login successful.")
                return user[0]
    #
    # Если нет - Invalid username or password.
            print("Invalid username or password.")
            return None

    except mysql.connector.Error as error:
        print(f"Database error: {error}")

        return None


def user_menu(connection, user_id):
    while True:
        print(text_user_menu.format(user_id=user_id))

        choice = input("Choose action: ").strip()

        if choice == "1":
            print("Book will be shown here.")

        elif choice == "2":
            print("Book search will be implemented here.")

        elif choice == "3":
            print("Book purchase will be implemented here.")

        elif choice == "4":
            print("Search statistics will be implemented here.")

        elif choice == "0":
            break

        else:
            print("Invalid option.")
        """
        Обрабатываем пользовательское меню из queries.py
        """



# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.
# 3
# Login as user
# Enter username: alex
# Enter password: 123
# Login successful.
#
# --- User Menu (ID 2) ---
#     1. View available books
#     2. Search books by title
#     3. Purchase a book
#     4. View most frequent search queries
#     0. Logout
# Choose action: 1
# Books will be shown here.
#
# --- User Menu (ID 2) ---
#     1. View available books
#     2. Search books by title
#     3. Purchase a book
#     4. View most frequent search queries
#     0. Logout
# Choose action: 0
#
# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.