from tkinter import *

root = Tk()
root.title("Стилизация")
root.geometry('200x350')

def red_color(event=None):
    root.configure(highlightbackground="red", highlightcolor="red", highlightthickness=3)

def green_color(event=None):
    root.configure(highlightbackground="green", highlightcolor="green", highlightthickness=3)

def blue_color(event=None):
    root.configure(highlightbackground="blue", highlightcolor="blue", highlightthickness=3)

def square_size(event=None):
    root.geometry('500x500')

def horizontal_size(event=None):
    root.geometry('700x400')

root.option_add("*tearOff", FALSE)

color_menu = Menu()
color_menu.add_command(label="Red", accelerator="r", command=red_color)
root.bind("<r>", red_color)
color_menu.add_command(label="Green", accelerator="g", command=green_color)
root.bind("<g>", green_color)
color_menu.add_command(label="Blue", accelerator="b", command=blue_color)
root.bind("<b>", blue_color)

size_menu = Menu()
size_menu.add_command(label = "500x500", accelerator="s", command=square_size)
root.bind("<s>", square_size)
size_menu.add_command(label = "700x400", accelerator="h", command=horizontal_size)
root.bind("<h>", horizontal_size)

settings_menu = Menu()
settings_menu.add_cascade(label="Color", menu=color_menu)
settings_menu.add_cascade(label="Size", menu=size_menu)

file_menu = Menu()
file_menu.add_cascade(label = "Настройки", menu=settings_menu)


root.config(menu=file_menu)

root.focus_set()
root.mainloop()
