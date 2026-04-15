import json

fruits_data = {
    "fruits" : {
        "яблоко" : 123,
        "апельсин" : 149,
        "лемон" : 92,
        "персик" : 115,
        "банан" : 160,
        "груша" : 120,
        "дыня" : 200
    }
}

with open("fruits_data.json", 'w', encoding='utf-8') as json_file:
    json.dump(fruits_data, json_file)