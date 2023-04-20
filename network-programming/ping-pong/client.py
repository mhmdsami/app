import socket

HOST = 'localhost'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = input('Enter a message: ')

client.sendall(message.encode('utf-8'))

data = client.recv(1024).decode()
print(data)

client.close()
