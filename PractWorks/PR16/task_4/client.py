import socket
from tkinter import *


def asdafdg():
    HOST = 'localhost'
    PORT = 50007

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    s.sendall(user_login.encode())

    while True:
        if user_message == "end":
            break

        data = f"{user_login}: {user_message}"
        s.sendall(data.encode())
    s.close()



root = Tk()
root.title("Клиент")
root.geometry('300x300')

log_entry = Entry()
message_entry = Entry()
btn = Button(text='Отправить', command=asdafdg)

user_login = log_entry.get()
user_message = message_entry.get()

log_entry.grid(columnspan=2)
message_entry.grid(columnspan=2)
btn.grid(columnspan=2)

root.mainloop()
