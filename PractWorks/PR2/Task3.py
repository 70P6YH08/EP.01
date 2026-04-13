year = int(input("Введите год: "))
month = int(input("Введите номер месяца: "))
days = 0
result_year = "Високосный" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "НЕ високосный"

if result_year == "Високосный":
    if month in (1,3,5,7,8,10,12):
        days = 31
        print(f"{year} високосный, {month} месяц, {days} день ")
    elif month in (4,6,9,11):
        days = 30
        print(f"{year} високосный, {month} месяц, {days} день ")
    else:
        days = 29
        print(f"{year} високосный, {month} месяц, {days} день ")
else:
    if month in (1,3,5,7,8,10,12):
        days = 31
        print(f"{year} НЕ високосный, {month} месяц, {days} день ")
    elif month in (4,6,9,11):
        days = 30
        print(f"{year} НЕ високосный, {month} месяц, {days} день ")
    else:
        days = 28
        print(f"{year} НЕ високосный, {month} месяц, {days} день ")