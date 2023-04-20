import socket

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

file_name = input('Enter the file name: ')

client.sendall(file_name.encode())

file_contents = client.recv(1024)

with open(file_name, 'wb') as f:
    f.write(file_contents)

client.close()
