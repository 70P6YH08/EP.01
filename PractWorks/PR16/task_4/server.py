from tkinter import *
import _thread
import socket
from datetime import datetime

def client_thread (conn):
    login = conn.recv(1024).decode('utf-8')
    log_label.config(f"Подключился логин:{login}\n")
    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        date_time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        print(f"{date_time}", data)
    conn.close()

HOST = ""
PORT = 50007




root = Tk()
root.title("СЕРВЕР")
root.geometry('400x300')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

log_label = Label()
while True:
    conn,addr = s.accept()
    _thread.start_new_thread(client_thread, (conn, ))


root.mainloop()
