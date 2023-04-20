import socket

HOST = 'localhost'
PORT = 8080

username = input('Enter username: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    data = input('Enter message: ')
    client.sendall(data.encode())
    data = client.recv(1024)
    print('Received', repr(data))