import socket

# Membuat socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Mengirim file ke server
with open('file_to_send.txt', 'rb') as file:
    data = file.read(1024)
    while data:
        client_socket.send(data)
        data = file.read(1024)

client_socket.close()
