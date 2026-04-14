import os

#Task 2
try:
    file_name = input("Введите название файла: ")

    if os.path.exists(file_name):
        file_text = input("Введите текст: ")
        print("Записать\t\t[w]\nДозаписать\t\t[a]")
        action = input()
        if action == "w":
            with open(file_name, "w") as file:
                file.write(file_text + "\n")
        elif action == "a":
            with open(file_name, "a") as file:
                file.write(file_text+"\n")
        else:
            print("Неизвестная команда")
    else:
        raise OSError
except OSError:
    print("Файл не найден")