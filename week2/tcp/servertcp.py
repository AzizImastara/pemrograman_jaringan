import socket

# Membuat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(5)

print("Waiting for connection...")
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Menerima file dari client
with open('received_file.txt', 'wb') as file:
    data = client_socket.recv(1024)
    while data:
        file.write(data)
        data = client_socket.recv(1024)


client_socket.close()
server_socket.close()
