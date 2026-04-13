
dictionary = {
    1:"Титёк",
    2:"Айфон",
    3:"Норд экспо",
    4:"Киви",
    5:"Банан",
    6:"Русификация",
    7:"Стол",
    8:"Лента",
    9:"Изолетна",
    10:"Клава",
    11:"Кока"
}

for key, value in dictionary.items():
    print(f"ключ: {key} - значение: {value}")

print()

key = int(input("Введите ключ из словаря: "))
if key in dictionary:
    print(f"ключ: {key} - значение: {dictionary[key]}")
else:
    print("Ключ не найден!")