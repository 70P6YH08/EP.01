
def checklist(n, mv, rv, iv):
    total = []
    for i in range(1, len(n) - 1):
        total.append((n[i], mv[i], rv[i], iv[i]))
    print(total)

names = ["Колян",
         "Вован",
         "Лерка",
         "Том Холланд",
         "Вуди Харрельсон",
         "Кружка",
         "Серёга пират",
         "На бабанах",
         "Окси",
         "Админ кристаликса"
         ]

math_value = [59,48,78,0,100,80,13,40,1,30]
rus_value = [20,10,72,0,100,50,28,101,1,40]
info_value = [35,39,54,0,100,70,0,21,1,90]

checklist(names,math_value,rus_value,info_value)
