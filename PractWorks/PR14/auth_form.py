from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Форма авторизации")

root.geometry('200x300')

loglbl = Label(root, text = "Логин")
passlbl = Label(root, text = "Пароль")

loglbl.grid()
passlbl.grid()

txt = Entry(root, width=10)
txt.grid(column =1, row =0)

txt = Entry(root, width=10)
txt.grid(column =1, row =1)

enabled = IntVar()

enabled_checkbutton = ttk.Checkbutton(text="Запомнить пароль", variable=enabled)
enabled_checkbutton.grid(column =0, row =2)

btn = ttk.Button(text="Авторизоваться")
btn.grid(column =0, row =3)

root.mainloop()