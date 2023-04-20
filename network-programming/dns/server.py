import socket

HOST = 'localhost'
PORT = 8080

dns_mappings = {
    '216.58.194.174': 'google.com',
    '131.13.76.102': 'facebook.com',
    '104.244.42.65': 'twitter.com',
    '199.96.56.231': 'linkedin.com'
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

while True:
    print('Waiting for a client to connect...')
    client, client_address = server.accept()
    print('Client connected:', client_address)

    ip_address = client.recv(1024).decode()

    if ip_address in dns_mappings:
        domain_name = dns_mappings[ip_address]
    else:
        domain_name = 'Cannot resolve domain name'

    client.sendall(domain_name.encode())

    client.close()
