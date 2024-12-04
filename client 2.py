import socket

socket_server = socket.socket()

# ipaddress = input("Введите ip")
# port = int(input("Введите порт"))
name = input("Введите имя ")


# socket_server.connect((str(ipaddress), port))
socket_server.connect(("127.0.0.1", 5050))
socket_server.send(name.encode())
socket_name = socket_server.recv(1024)
server_name = socket_name.decode()
print(server_name, "Присоединился")


while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Я: ")
    socket_server.send(message.encode())
