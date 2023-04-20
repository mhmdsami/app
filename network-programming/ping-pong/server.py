import socket

HOST = 'localhost'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

conn, addr = server.accept()
print('Connected by', addr)

data = conn.recv(1024).decode()

if data == 'ping':
    conn.sendall('pong'.encode('utf-8'))

conn.close()
