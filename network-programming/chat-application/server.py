import socket

HOST = 'localhost'
PORT = 8080

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

while True:
    client, address = server.accept()
    clients.append(client)
    
    print('Connected by', address)

    while True:
        data = client.recv(1024)
        if not data:
            break
        client.sendall(data)
