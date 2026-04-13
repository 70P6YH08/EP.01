def print_hello(name = "World"):
    print(f"Hello, {name}")

def convert_base(n, base, digits="0123456789ABCDEF"):
    if n < base:
        return digits[n]
    else:
        return convert_base(n // base, base) + digits[n % base]

def print_text(text):
    str_text = ""
    for i in text:
        str_text = str_text + i
        if i in "?!.":
            str_text = str_text + "\n"
            print(str_text.strip())
            str_text = ""

def cezar(text, key = 3):
    count = 0
    mass_str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    text = text.lower()
    for i in text:
        while i != mass_str[count]:
            count+=1
            if count + key == 33:
                count = -key
        else:
            if i == " ":
                i = mass_str[count]
            else:
                i = mass_str[count + key]
            count = 0
        print(i, end='')
    print("")
