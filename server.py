import socket
import threading
import os

log_filename = "servers_messages.log"
MAX_CLIENTS = 5
clients = {}
def handle_client(client_socket):
    if os.path.exists(log_filename):
        with open(log_filename, "r") as log_file:
            lines = log_file.readlines()[-10:]
            for line in lines:
                client_socket.send(line.encode())

    while True:
        message = client_socket.recv(1024).decode()

        with open(log_filename, "a") as log_file:
            log_file.write(message + "\n")

        broadcast_message(message, client_socket)
def broadcast_message(message, client_socket):
    for client in list(clients):
        if client != client_socket:
            try:
                client.send(message.encode())
            except:
                del clients[client]

def start_server():
    new_socket = socket.socket()
    new_socket.bind(("127.0.0.1", 5050))
    new_socket.listen(MAX_CLIENTS)

    print("Сервер запущен")
    print("Сервер ожидает подключения...")

    while True:
        if len(clients) >= MAX_CLIENTS:
            print(f"Max amount of peolple is {MAX_CLIENTS}")
            continue
        client_socket, client_address = new_socket.accept()
        print(f"Подключился клиент с адресом {client_address}")

        clients[client_socket] = client_address

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()