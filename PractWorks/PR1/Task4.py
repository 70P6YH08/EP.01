"""Task 4"""

num = int(input("Введите целое число: "))

print(f"В десятичной: {num}")
print(f"В двоичной: {bin(num)[2:]}")
print(f"В восьмеричной: {oct(num)[2:]}")
print(f"В шестнадцатеричной: {hex(num)[2:]}")
print()
print(f"В десятичной: {num}")
print(f"В двоичной: {format(num, 'b')}")
print(f"В восьмеричной: {format(num, 'o')}")
print(f"В шестнадцатеричной: {format(num, 'x')}")