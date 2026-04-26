from tkinter import *
from tkinter import filedialog


def open_file_dialog(event=None):
    filedialog.asksaveasfilename()

def destroy_dialog(event=None):
    root.destroy()

root = Tk()
root.title("Task 1")
root.geometry("250x250")

text = Text(height = 5)
text.pack()

save_bth = Button(text = "Сохранить", command=open_file_dialog)
save_bth.bind_all("<Control-s>", open_file_dialog)
save_bth.pack()

root.bind('<Escape>', destroy_dialog)

root.mainloop()