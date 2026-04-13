print("Вопрос?")

answer = input("Ответ: ")

rAnswer = answer.lower()

if rAnswer == "нет":
    print(True)
else:
    print(False)