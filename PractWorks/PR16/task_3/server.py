import _thread
import socket
from datetime import datetime

HOST = ""
PORT = 50007

def client_thread (conn):
    login = conn.recv(1024).decode('utf-8')
    print("Подключился логин:", login)
    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        date_time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        print(f"{date_time}", data)
    conn.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn,addr = s.accept()
    _thread.start_new_thread(client_thread, (conn, ))