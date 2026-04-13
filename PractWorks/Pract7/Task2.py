def fact(n):
    try:
        if n < 0:
            raise ValueError
        if n > 1:
            n = n * fact(n - 1)
        return n
    except ValueError:
        return -1
    except TypeError:
        return -1

print(fact(3))