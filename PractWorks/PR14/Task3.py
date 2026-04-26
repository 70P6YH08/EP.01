from tkinter import *
from tkinter import ttk


def info():
    text = f"{txt_str_var.get()}, {check_b_int_var.get()}, {radio_b_str_var.get()}"
    lbl_info_var.set(text)

root = Tk()

root.title("Форма регистрации")
root.geometry('200x350')

txt_str_var = StringVar()
txt = Entry(root, textvariable=txt_str_var)

check_b_int_var = IntVar()
enabled_checkbutton = Checkbutton(text="Я согласен", variable=check_b_int_var)

man = "Муж"
woman = "Жен"
radio_b_str_var = StringVar(value=man)
men_btn = Radiobutton(text=man, value=man, variable=radio_b_str_var)
women_btn = Radiobutton(text=woman, value=woman, variable=radio_b_str_var)


lbl_info_var = StringVar()
lbl_info = Label(textvariable = lbl_info_var)

btn_lbl_info = Button(text="Обновить значения", command=info)


txt.grid(columnspan=2)

root.columnconfigure(0, weight=1)

enabled_checkbutton.grid(columnspan=2)

men_btn.grid(row = 4, columnspan=2)
women_btn.grid(row = 5, columnspan=2)

lbl_info.grid(row=6, columnspan=2)
btn_lbl_info.grid(row=7, columnspan=2)


root.mainloop()