books = {
    1 : "Роман какой-то",
    2 : "Мышь",
    3 : "Ковёр самолёт скороход",
    4 : "Часики то тикают",
    5 : "Лампа",
    6 : "Мари Фантено",
    7 : "Тэд Чилдрес",
    8 : "Ошибка",
    9 : "Родственница",
    10 : "Начальник, ты просто босс",
    11 : "1990",
    12 : "Ребёнок",
    13 : "Дело"
}
flag = True

try:
    while flag == True:
        try:
            input_action = input(f"Введите действие:"
                                 f"\nСоздать\t\t[cre]"
                                 f"\nПросмотр\t[view]"
                                 f"\nУдалить\t\t[del]"
                                 f"\nВыход\t\t[esc]\n")
            if input_action == "del":
                key = int(input("Ключ: "))
                del books[key]
            elif input_action == "cre":
                key = int(input("Ключ: "))
                name = input("Введите название книги: ")
                books[key] = name
            elif input_action == "view":
                for k,v in books.items():
                    print(f"{k} - {v}")
                print("\n")
            elif input_action == "esc":
                flag = False
        except KeyError:
            print("Такого ключа нет")
finally:
    print("Программа звершена")