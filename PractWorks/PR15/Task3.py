from tkinter import *

def mouse_motion(event):
    x = event.x
    y = event.y
    label_var.set(f"Координаты мыши: x:{x}, y:{y}")

root = Tk()
root.title("Task 3")
root.geometry("250x250")

label_var = StringVar()
label = Label(textvariable=label_var, font="Times 50")
label.pack(fill=BOTH, expand=1)

label.bind("<Motion>", mouse_motion)

root.mainloop()