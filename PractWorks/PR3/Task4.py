summa = int(input("Сумма покупки: "))
user_sum = int(input("Сумма, внесённая покупателем: "))

while summa <= 0:
    print("Повторите ввод суммы покупки")
    summa = int(input())

while user_sum < summa:
    summa -= user_sum
    print(f"Добавьте деньги. Не хватает {summa}")
    user_sum = int(input())

if user_sum == summa:
    print("Спасибо!")
else:
    print(f"Возьмите сдачу: {user_sum - summa}")