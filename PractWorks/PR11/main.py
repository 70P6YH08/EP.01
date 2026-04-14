import re
from re import split

#Task 1
text = "Как же это бесит, когда кто-то... Лезет с хамством и злобой? Сердце разрывается от несправедливости. Но хватит! Пусть все эти редиски и нехорошие люди исчезнут!! Хочется наконец тепла и улыбок??? Давайте жить дружно — вот единственное спасение от всей этой дурацкой злости."
result = re.split(r'[.?!]+', text)
for i in result:
    print(i.strip())

#Task 2
text_task2 = "Однажды я вырастил на грядке большую красную редиску. Но пришёл сосед — настоящий нехороший человек. Этот нехороший человек выдернул мою редиску и съел. Я говорю: «Ты просто редиска, а не человек!» А он смеётся: «Редиска — это вкусно, а вот ты — нехороший человек, потому что обзываешься». Так мы и расстались: я без редиски, а он — нехороший человек при редиске."

result_rediska = re.sub(r'редиск\w+', "*давайте жить дружно*", text_task2)
result_task2 = re.sub(r'нехорош\w+\s+челов\w+', "*давайте жить дружно*", result_rediska)
print(result_task2)

#Task 3
text_date = "01-02-2024, 30.11.02 2/2/23, 31.7.324, asdw, asda2, 2as, asd2, saa2345, 23-24-526, 23.12.2024, 02-11.23, 32.11.12, 31.13.2024"
date_pattern  = r'\b(?:0?[1-9]|[12]\d|3[01])\b\.\b(?:0?[1-9]|1[0-2])\b\.\b(?:\d{2}|\d{4})\b'
# replace_pattern = r'[-/]'
# replace_result = re.sub(replace_pattern, ".", text_date)
findall_result = re.findall(date_pattern, text_date)
for i in findall_result:
    print(i)

print("")

#Task 4

password = input("")
password_pattern = r'\b(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\W]{6,}\b'

while True:
    if re.search(password_pattern, password):
        print(f"Успешно: {password}")
        break
    else:
        password = input("Повторно введите пароль: ")

