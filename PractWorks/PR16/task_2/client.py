import socket
HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall('Hello, world'.encode())

while True:
    message = input("Введите сообщение: ")
    if message == "end":
        break

    s.sendall(message.encode())
s.close()