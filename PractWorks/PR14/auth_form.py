from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Форма авторизации")

root.geometry('200x300')

loglbl = Label(root, text = "Логин")
passlbl = Label(root, text = "Пароль")

logtxt = Entry(root)
passtxt = Entry(root)

loglbl.grid(column =0, row =0)
passlbl.grid(column =0, row =1)

root.columnconfigure(0, weight=1)

logtxt.grid(column =1, row =0)
passtxt.grid(column =1, row =1)

root.columnconfigure(1, weight=1)

enabled = IntVar()

enabled_checkbutton = Checkbutton(text="Запомнить пароль", variable=enabled)
enabled_checkbutton.grid(column =0, row =2, columnspan=2)

btn = Button(text="Авторизоваться")
btn.grid(column =0, row =3, columnspan=2)

root.mainloop()