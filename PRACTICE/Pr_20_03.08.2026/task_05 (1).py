""" 05 Повторный ввод при ошибке

Модифицируйте программу так, чтобы при вводе некорректного номера департамента
    пользователю предлагалось ввести его снова.
Программа не должна завершаться, пока не будет введён корректный номер.

Пример вывода:
Enter department number: 999
Invalid department number. Please try again.
Enter department number: num1
Invalid input. Please enter a number.
Enter department number: 2
You selected: Marketing
"""

import mysql.connector
from local_settings import dbconfig

dbconfig['database'] = 'hr'

pass




