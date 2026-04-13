a = int(input("1 число: "))
b = int(input("2 число: "))

op = input("Операция: ")

if op == "&":
    print(f"{a} {op} {b} = {bin(a & b)[2:]}")
elif op == "|":
    print(f"{a} {op} {b} = {bin(a | b)[2:]}")
elif op == "^":
    print(f"{a} {op} {b} = {bin(a ^ b)[2:]}")
elif op == "<<":
    print(f"{a} {op} {b} = {bin(a << b)[2:]}")
elif op == ">>":
    print(f"{a} {op} {b} = {bin(a >> b)[2:]}")
else:
    print("Неизвестная операция")
