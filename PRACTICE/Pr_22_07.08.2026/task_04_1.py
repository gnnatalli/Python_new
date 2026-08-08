""" 4.1. Просмотр книг в наличии

Добавьте в дополнительное меню клиента пункт,
который позволяет просмотреть все доступные книги в магазине.
Должны отображаться только книги, у которых количество больше 0;
Для каждой книги выводите: название, автора, цену и остаток на складе;
Вывод сопровождается нумерацией (не ID из базы, а порядковый номер).
Пример вывода:
Available books:
1. 1984 by George Orwell — $8.99 (5 in stock)
2. Brave New World by Aldous Huxley — $9.50 (3 in stock)
"""

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

"""Добавьте как пункт 1 в user_menu:"""


