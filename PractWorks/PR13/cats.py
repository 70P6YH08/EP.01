import json
import os.path


class Cat:
    name : str
    age : int
    color : str
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

cats_data = {
    "cats" : [

    ]
}
if not os.path.exists("cats_data.json"):
    with open("cats_data.json", 'w', encoding='utf-8') as json_file:
        json.dump(cats_data, json_file)

while True:
    try:
        with open("cats_data.json", 'r', encoding='utf-8') as json_file:
            cats_data = json.load(json_file)
    except FileNotFoundError:
        cats_data = {"cats": []}

    print("\tДействия:\t\n"
          "1\t\tДобавить\n"
          "2\t\tПросмотреть\n"
          "3\t\tУдалить\n"
          "4\t\tВыйти\n"
          "5\t\tСортировать\n")
    action = input("")
    if action == "1":
        while True:
            cat_name = input("Введите имя: ")
            cat_age = input("Введите возраст: ")
            cat_color = input("Введите цвет: ")
            new_cat = Cat(cat_name, cat_age, cat_color)

            new_data_cat = new_cat.__dict__

            cats_data["cats"].append(new_data_cat)

            with open("cats_data.json", 'w', encoding='utf-8') as json_file:
                json.dump(cats_data, json_file)

            action = input("Продолжить?\t[y/n]\n")
            if action == "n":
                break
    elif action == "2":
        count = 1
        for i in cats_data['cats']:
            print(f"{count} кот: ", end='')
            count +=1
            for k,v in i.items():
                print(f"{k} - {v}", end=', ')
            print("")
    elif action == "3":
        count = 1
        val = input("Имя: ")
        for i in cats_data['cats']:
            if i.get('name') == val:
                cats_data['cats'].remove(i)
                break

        with open("cats_data.json", 'w', encoding='utf-8') as json_file:
            json.dump(cats_data, json_file)
        print("")

    elif action == "4":
        break

    elif action == "5":
        print("\tСортировка\n"
              "1\t\tПо имени\n"
              "2\t\tПо возрасту\n")
        action = input("")
        if action == "1":
            cats_data['cats'] = sorted(cats_data["cats"], key=lambda x: x["name"].lower())

        elif action == "2":
            cats_data['cats'] = sorted(cats_data["cats"], key=lambda x: int(x["age"]))

        else:
            print("Неизвестная команда")

        with open("cats_data.json", 'w', encoding='utf-8') as json_file:
            json.dump({"cats" : cats_data["cats"]}, json_file)

    else:
        print("Неизвестная команда")