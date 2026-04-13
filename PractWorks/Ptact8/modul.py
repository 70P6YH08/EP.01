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
        if i in "?!...":
            str_text = str_text + "\n"
            print(str_text.strip())
            str_text = ""

print_text("daasda. da dasd asd as d. asd a? sdad sa")