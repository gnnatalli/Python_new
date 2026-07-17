""" 01 План по дням недели

Напишите программу, которая помогает планировать дела.
Программа должна
- бесконечно выводить план на следующий день недели,
- пока пользователь нажимает 'Enter'.

Данные:
# Расписание дел на неделю
weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

Пример ввода:
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана:
Tuesday: Meeting, Work, Study Python
...
Нажмите 'Enter' для получения плана:
Sunday: Family time, Rest
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана: q
"""
from itertools import cycle

weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

# cycle(weekly_schedule) - бесконечно повторяет дни недели
days = cycle(weekly_schedule)

for day in days:
    unser_input = input("Нажмите 'Enter' для получения плана (или 'q' для выхода): ")

    # q - выход из программы
    if unser_input == 'q':
        break
    # join() - красиво выводит список дел через запятую
    print(f"{day}: {','.join(weekly_schedule[day])}")
