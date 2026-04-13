word = input("Введите слово: ")

rw = word.lower()
rrw = ""

wl = len(word)

for i in range(wl - 1, 0 - 1, -1):
    rrw = rrw + rw[i]

flag = True

if wl % 2 == 0:
    fpw = wl / 2
    for i in range(0, wl -1):
        if rrw[i] != rw[i]:
            flag = False
            break
else:
    fpw = wl // 2
    for i in range(0, wl - 1):
        if rrw[i] != rw[i]:
            flag = False
            break

if flag == True:
    print(True)
else:
    print(False)