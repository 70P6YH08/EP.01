import os
import re

#Task 5
try:
    file_name = input("Введите название файла: ")

    if os.path.exists(file_name):
        with open(file_name, 'r', encoding="utf-8") as file:
            list_str = []
            replace_trim = r'\s+'
            digital_pattern = r'\d+'
            for line in file:
                summa = 0
                # numbers = list(map(int, line.split()))
                # print(sum(numbers))
                list_str.append(re.sub(replace_trim, " ", line.strip()))
                for i in range(0, len(re.sub(replace_trim, " ", line.strip())) - 1):
                    summa = summa + i
                    print(summa)


    else:
        raise OSError
except OSError:
    print("Файл не найден")