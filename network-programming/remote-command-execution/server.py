import socket

HOST = 'localhost'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

conn, addr = server.accept()
print('Connected by', addr)

conn.sendall(b'dir')

conn.close()
