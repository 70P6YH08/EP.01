from tkinter import *
from tkinter import ttk


def update_label():
    string_value = string_var.get()
    check_value = check_var.get()
    radio_value = radio_var.get()

    display_text = f"{string_value}, {check_value}, {radio_value}"
    alllbl.config(text=display_text)


root = Tk()

string_var = StringVar()
check_var = IntVar()
radio_var = IntVar(value=1)


root.title("Task 3")

root.geometry('200x350')

txt = Entry(root, width=10, textvariable=string_var)
txt.grid(column =0, row =0)


enabled_checkbutton = Checkbutton(root,
                                      text="Флажок",
                                      textvariable=check_var,
                                      command=update_label)

enabled_checkbutton.grid(column =1, row =0)

man = "Муж"
woman = "Жен"


python1 = Radiobutton(text=man,
                             value=man,
                             textvariable=radio_var,
                             command=update_label)
python1.grid(row = 3)

python2 = Radiobutton(text=woman,
                             value=woman,
                             textvariable=radio_var,
                             command=update_label)
python2.grid(row = 4)

alllbl = Label(root, text = "", width=20)
alllbl.grid(column =0, row =6)

txt.bind("<KeyRelease>", lambda event: update_label())

root.mainloop()