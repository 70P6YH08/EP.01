from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Форма регистрации")
root.geometry('200x350')
root.configure(bg='lightblue')


loglbl = Label(root, text = "Логин", background="green")
passlbl = Label(root, text = "Пароль", background="green")

logtxt = Entry(root)
passtxt = Entry(root)

aboutme = Label(root, text = "О себе", background="green")
editor = Text(height=5, width=25)

man = "Муж"
woman = "Жен"
gender = StringVar(value=man)
header = Label(textvariable=gender, background="green")
men_btn = Radiobutton(text=man, value=man, variable=gender, background="lightblue")
women_btn = Radiobutton(text=woman, value=woman, variable=gender, background="lightblue")

languages = ["Сервеная Америка","Южная Америка","Евразия","Африка","Австралия"]
languages_var = Variable(value=languages)
languages_listbox = Listbox(listvariable=languages_var, height=5, bg="yellow")

btn = Button(text="Зарегистрироваться", background="green")



loglbl.grid(column =0, row =0)
passlbl.grid(column =0, row =1)

logtxt.grid(column =1, row =0)
passtxt.grid(column =1, row =1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

aboutme.grid(columnspan=2, row =3)
editor.grid(column =0, row =4, columnspan = 2)

header.grid(row = 5, columnspan=2)
men_btn.grid(row = 6, columnspan=2)
women_btn.grid(row = 7, columnspan=2)

languages_listbox.grid(columnspan=2, row =8)

btn.grid(column =0, row =9, columnspan=2)

root.mainloop()