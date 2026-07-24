""" 4. Карточка студента

Добавьте метод show_info(), который выводит информацию о студенте на текущий момент.
Возраст вычисляется автоматически на основе даты рождения.

Пример вывода:
Student:
	Name: Alice
	Age: 19
	ID: 1

"""



# Перерасчёт даты рождения от сегодняшней даты, чтобы Алисе всегда было 19
alis_birthday = (datetime.today() - relativedelta(years=19)).date().__str__()  #2006-12-07"

s1 = Student("Alice", alis_birthday)
s1.show_info()

# Student:
#     Name: Alice
#     Age: 19
#     ID: 1