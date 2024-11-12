import socket

HOST = '127.0.0.1'
PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT)) #подключаемся к серверу

while True:
    #получаем сообщение от сервера
    server_message = client_socket.recv(1024).decode()
    print(f"Сервер: {server_message}")

    #отправляем сообщение серверу
    client_message = input("Вы: ")
    client_socket.send(client_message.encode())

