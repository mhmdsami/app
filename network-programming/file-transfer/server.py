import socket

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

while True:
    print('Waiting for a client to connect...')
    client_socket, client_address = server.accept()
    print('Client connected:', client_address)

    file_name = client_socket.recv(1024).decode()

    with open(file_name, 'rb') as f:
        file_contents = f.read()
        client_socket.sendall(file_contents)

    client_socket.close()
