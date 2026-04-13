def fact(n):
    try:
        if n < 0:
            raise ValueError
        elif n == 0 or n == 1:
            return 1
        elif n > 1:
            breakpoint()
            n = n * fact(n - 1)
        return n
    except TypeError:
        return "Неправильный тип данных"
    except ValueError:
        return "Отрицательное значение"

if __name__ == "__main__":
    print(fact(4))