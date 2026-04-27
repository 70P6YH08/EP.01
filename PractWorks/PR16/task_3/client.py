import socket

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

user_login = ""
while len(user_login) < 1:
    user_login = input("Введите свой логин: ")

s.connect((HOST, PORT))
s.sendall(user_login.encode())

while True:
    message = input("Введите сообщение: ")
    if message == "end":
        break
    
    data = f"{user_login}: {message}"
    s.sendall(data.encode())
s.close()