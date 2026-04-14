import os

#Task 3
try:
    file_name = input("Введите название файла: ")

    if os.path.exists(file_name):
        print("Вывод содержимого\t[read]\n"
              "Удаление файла\t\t[del]\n"
              "Переименовать\t\t[ren]\n")
        action = input()
        if action == "read":
            with open(file_name, 'r') as file:
                for line in file:
                    print(line)
        elif action == "del":
            os.remove(file_name)
        elif action == "ren":
            new_file_name = input("Введите новое имя файла: ")
            os.rename(file_name, new_file_name)
        else:
            print("Неизвестная команда")
    else:
        raise OSError
except OSError:
    print("Файл не найден")