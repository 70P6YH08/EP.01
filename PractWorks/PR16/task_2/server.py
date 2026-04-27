import socket
from datetime import datetime

HOST = ""
PORT = 50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn,addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        date_time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        print(f"{date_time} {addr}:", data.decode('utf-8'))
    conn.close()