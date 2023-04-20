import socket

HOST = 'localhost'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

ip_address = input('Enter the IP address: ')

client.sendall(ip_address.encode())
domain_name = client.recv(1024).decode()

print('Domain name:', domain_name)

client.close()
