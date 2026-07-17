import os
from datetime import date

from unicodedata import category

# 1. Читаем файл и превращаем строки в словари
def read_file(file_name):
    sales = []

    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            name, date, amount, category, city = line.strip().split(",")

            year = date[:4]
            month = date[5:7]

            sales.append({
                "name": name,
                "date": date,
                "amount": amount,
                "category": category,
                "city": city,
                "year": year,
                "month": month
            })
    return sales

# 2. Группируем данные
def group_sales(sales):
    grouped_sales = {}
    category_totals = {}

    for sale in sales:
        year = sale["year"]
        month = sale["month"]
        category = sale["category"]
        amount = sale["amount"]

        # ключ для группировки по категории
        key = (year, month, category)

        if key not in grouped_sales:
            grouped_sales[key] = []

        grouped_sales[key].append(sale)

            # ключ для месячных итогов
        month_key = (year, month)

        if month_key not in category_totals:
            category_totals[month_key] = {}

        if category not in category_totals[month_key]:
            category_totals[month_key][category] = 0

        category_totals[month_key][category] += amount

    return grouped_sales, category_totals

# 3. Создание папок
def create_folders(output_dir, category_totals):
    for year, month in category_totals:
        path = os.path.join(output_dir, year, month)
        os.makedirs(path, exist_ok=True)

# 4. Запись monthly_report.txt
def write_monthly_report(output_dir, category_totals):
    for (year, month), categories in category_totals.items():

        folder = os.path.join(output_dir, year, month)
        file_path = os.path.join(folder, "monthly_report.txt")

        total = 0

        with open(file_path, "w", encoding="utf-8") as file:
            for category, amount in categories.items():
                file.write(f"{category}: {amount}\n")
                total += amount

            file.write(f"Full, {total}")

# 5. Запись файлов по категориям
def write_category_files(output_dir, grouped_sales):
    for (year, month, category), sales in grouped_sales.items():

        folder = os.path.join(output_dir, year, month)
        file_path = os.path.join(folder, f"{category}.txt")

        # сортировка по дате
        sales.sort(key=lambda x: x["date"])

        with open(file_path, "w", encoding="utf-8") as file:
            for sale in sales:
                file.write(f"{sale['date']}-{sale['name']}-{sale['amount']}\n")


# 6. Главная функция

