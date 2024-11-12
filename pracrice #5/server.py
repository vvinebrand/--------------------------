import socket

HOST = '127.0.0.1'
PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создаем сокет для сервера при помощи IPv4 и TCP
server_socket.bind((HOST, PORT)) #привязывем сокет к хосту и порту
server_socket.listen() #прослушиваем входящие подключения
print("Сервер запущен и ожидает подключения...")

client_socket, addr = server_socket.accept() #возвращаем сокет и адрес для общения с клиентом
print(f"Подключен к {addr}")

while True:
    #отправляем сообщение клиенту
    server_message = input("Сервер: ")
    client_socket.send(server_message.encode())
    
    #получаем сообщение от клиента
    client_message = client_socket.recv(1024).decode()
    print(f"Клиент: {client_message}")

