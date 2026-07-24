""" 06. Возраст на конкретную дату

Добавьте метод calculate_age_on(target_date: datetime), который позволяет
получить возраст студента на переданную дату.

"""




# Перерасчёт даты рождения от сегодняшней даты, чтобы Алисе всегда было 19
alis_birthday = (datetime.today() - relativedelta(years=19)).date()  #2006-12-07"

s1 = Student("Alice", str(alis_birthday))

# День рождения Алисы через 25 лет
alis_birthday_plus_25 = alis_birthday + relativedelta(years=25)

print(s1.calculate_age_on(alis_birthday_plus_25))
# 25