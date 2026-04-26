from tkinter import *

current_entry = None

def focus(event=None):
    global current_entry
    current_entry = event.widget

def left_click(event=None):
    label_text = current_entry.get()
    label_var.set(label_text)

def right_click(event=None):
    print(current_entry.get())

root = Tk()
root.title("Task 2")
root.geometry("250x250")


entry1 = Entry()
entry2 = Entry()
entry3 = Entry()
entry1.pack()
entry2.pack()
entry3.pack()

label_var = StringVar()
label = Label(textvariable=label_var)
label.pack()
label.focus_set()

root.bind_class("Entry", "<Double-ButtonPress-1>", left_click)
root.bind_class("Entry", "<ButtonPress-3>", right_click)
root.bind_class("Entry", "<Enter>", focus)

root.mainloop()