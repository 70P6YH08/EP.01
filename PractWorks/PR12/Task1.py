import os

#Task 1
try:
    file_name = input("Введите название файла: ")

    ext_file = os.path.splitext(file_name)
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                print(line)
        if ext_file[1] ==".py":
            os.system(f"python {file_name}")
    else:
        raise OSError
except OSError:
    print("Файл не найден")