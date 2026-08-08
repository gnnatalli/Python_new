import mysql.connector
from queries import text_user_menu

def load_books_from_file(filename, connection, db_name):
    added = 0  # подсчитываем кол-во добавленных книг
    with open(filename, "r", encoding="utf-8") as file:   # открываем файл
        with connection.cursor() as cursor:
            cursor.execute(f"USE `{db_name}`")
            line = file.readline()

            for line in file:
                parts = line.split(",")


                if len(parts) != 4:
                    continue  # пропускаем некорректные строки файла


                title, author, price_text, stock_text = parts
                try:
                    price = float(price_text)
                    stock = int(stock_text)
                except ValueError:
                    continue


                # Проверка: есть ли такая книга
                cursor.execute(
                    "SELECT id FROM books WHERE title = %s AND author = %s",
                    (title, author),
                )
                book = cursor.fetchone() # tulpe

                # Если есть - добавляем кол-во из файла к тому, что уже есть
                if book is not None:
                    cursor.execute(
                        "UPDATE books SET stock = stock + %s WHERE id = %s",
                        (stock, book[0]),
                    )
                else:
                    # Если нет - добавляем книгу и увеличиваем счётчик добавленных
                    cursor.execute(
                        "INSERT INTO books (title, author, price, stock) VALUES (%s, %s, %s, %s)",
                        (title, author, price, stock),
                    )

                added += 1

    print(f"{added} books loaded.")


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


def user_menu(connection, user_id, db_name):
    while True:
        print(text_user_menu.format(user_id=user_id))

        choice = input("Choose action: ").strip()

        if choice == "1":
            view_available_books(
                connection,
                user_id,
                db_name
            )

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


def show_available_books(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, title, author, price, stock
            FROM books
            WHERE stock > 0
            ORDER BY title
            """
        )

        books = cursor.fetchall()

        if not books:
            print("No books available.")
            return

        print("\nAvailable books:")

        for book in books:
            print(
                f"ID: {book[0]} | "
                f"Title: {book[1]} | "
                f"Author: {book[2]} | "
                f"Price: {book[3]} | "
                f"Stock: {book[4]}"
            )

def view_available_books(connection, user_id, db_name):
    with connection.cursor() as cursor:
        cursor.execute(f"USE `{db_name}`")

        cursor.execute(
            """
            SELECT title, author, price, stock
            FROM books
            WHERE stock > 0
            """
        )

        books = cursor.fetchall()

        if not books:
            print("No books available.")
            return

        print("\nAvailable books:\n")

        for number, book in enumerate(books, start=1):
            title, author, price, stock = book

            print(
                f"{number}. {title} by {author} — "
                f"${price:.2f} ({stock} in stock)"
            )