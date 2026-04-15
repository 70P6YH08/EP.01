from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Форма регистрации")

root.geometry('200x350')
root.configure(bg='lightblue')

loglbl = Label(root, text = "Логин", background="lightgray")
passlbl = Label(root, text = "Пароль", background="lightgray")
aboutme = Label(root, text = "О себе", background="lightgray")

languages = ["Сервеная Америка",
             "Южная Америка",
             "Евразия",
             "Африка",
             "Австралия"]
languages_var = Variable(value=languages)

languages_listbox = Listbox(listvariable=languages_var, height=5, bg="blue")

btn = ttk.Button(text="Зарегистрироваться")


loglbl.grid()
passlbl.grid()
aboutme.grid()

txt = Entry(root, width=10)
txt.grid(column =1, row =0)

txt = Entry(root, width=10)
txt.grid(column =1, row =1)

editor = Text(height= 5, width=25)
editor.grid(column =0, row =3, columnspan = 2)

languages_listbox.grid(column =0, row =7)

btn.grid(column =0, row =8)


man = "Муж"
woman = "Жен"

sex = StringVar(value=man)

header = ttk.Label(textvariable=sex, background="lightgray")
header.grid(row = 4)

python_btn = ttk.Radiobutton(text=man, value=man, variable=sex)
python_btn.grid(row = 5)

python_btn = ttk.Radiobutton(text=woman, value=woman, variable=sex)
python_btn.grid(row = 6)

root.mainloop()