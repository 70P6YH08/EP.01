class Author:
    def __init__(self, full_name, country):
        self.full_name = full_name
        self.country = country

    def print_info(self):
        print(f"ФИО: {self.full_name}, страна: {self.country}")

n = int(input("Введите количество авторов:"))
print("")

list_authors = [ ]


while n > 0:
    f_n = input("ФИО автора: ")
    c = input("Страна: ")
    list_authors.append(Author(f_n, c))
    n -= 1

print("Все авторы:")

for i in list_authors:
    i.print_info()

print("")
print("Только НАШИ авторы:")

for i in list_authors:
    if i.country == "Россия":
        i.print_info()