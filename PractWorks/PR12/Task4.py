import os

#Task 4
try:
    file_name = input("Введите название файла: ")

    if os.path.exists(file_name):
        print("1-ая строка\t\t\t[1s]\n"
              "5-ая строка\t\t\t[5s]\n"
              "Первые 5 строк\t\t[1-5s]\n"
              "С n по m строки\t\t[nm]\n"
              "Весь файл\t\t\t[allw]\n")
        action = input()
        if action == "1s":
            with open(file_name, 'r', encoding="utf-8") as file:
                str1 = file.readline()
                print(str1)
        elif action == "5s":
            with open(file_name, 'r', encoding="utf-8") as file:
                file_text = file.readlines()
                str1 = file_text[4]
                print(str1)
        elif action == "1-5s":
            with open(file_name, 'r', encoding="utf-8") as file:
                for i in range(0,5):
                    print(file.readline(), end="")
        elif action == "nm":
            with open(file_name, 'r', encoding="utf-8") as file:
                n = int(input("Введите первую позицию: "))
                m = int(input("Введите вторую позицию: "))
                file_text = file.readlines()
                for i in range(n,m + 1):
                    str1 = file_text[i - 1]
                    print(str1, end="")
        elif action == "allw":
            with open(file_name, 'r', encoding="utf-8") as file:
                print(file.read())
        else:
            print("Неизвестная команда")
    else:
        raise OSError
except OSError:
    print("Файл не найден")