rus = [123,31,23,52,12,26,26,147,124,2,52,6,12,72]
math = [234,52,247,47,2,485,86,93,4,5,63,361,73,84]
inf = [432,25,12,36,27,4,82,4,85,224,2,74,89,4]

abb = [
    "Вован",
    "Колян",
    "Антоха",
    "Маша",
    "Валя",
    "Эдик",
    "Базанов",
    "Ознобихин",
    "Марина",
    "Арменка",
    "Мама",
    "Лерка",
    "Серёжа",
    "Медичка"
]

students = [

]

for i in range(0, len(abb) - 1):
    total = rus[i] + math[i] + inf[i]
    students.append((i, abb[i], total))

def max_sum(students):
    return students[2]

studentsTop = sorted(students, key = max_sum, reverse=True)[:10]
print("Поступили:")
for index, name, total in studentsTop:
    print(f"{index} - {name}")