import json
import os


class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

cats = []

if os.path.exists("cats_data.json"):
    with open("cats_data.json", "r", encoding='utf-8') as json_file:
        cats_data = json.load(json_file)
        cats = cats_data

while True:
    cat_name = input("Введите имя: ")
    cat_age = input("Введите возраст: ")
    cat_color = input("Введите цвет: ")
    cat = Cat(cat_name, cat_age, cat_color)

    cats.append({
        "Имя" : cat.name,
        "Возраст" : cat.age,
        "Цвет" : cat.color
    })

    with open("cats_data.json", "a", encoding='utf-8') as json_file:
        json.dump(cats, json_file)

    action = input("Продолжить?\t[y]\t[n]\n")
    if action == "n":
        break

