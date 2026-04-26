from tkinter import *

def key_update_label(event):
    char = event.char
    text = label_var.get()
    label_var.set(text + char)

root = Tk()
root.title("Task 4")
root.geometry("250x250")

label_var = StringVar(value = "Нажатые клавиши:")
label = Label(textvariable=label_var,
              text = "Нажатые клавиши: ",
              font="Times 50")
label.pack()
label.focus_set()

label.bind("<Key>", key_update_label)

root.mainloop()