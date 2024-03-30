import socket

# membuat objek socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# mengikat socket server ke alamat dan port tertentu
server_address = ('localhost', 8000)
server_socket.bind(server_address)

# mengaktifkan socket server agar dapat menerima koneksi
server_socket.listen(1)

# menerima koneksi dari socket client
print('Waiting for a connection...')
client_socket, client_address = server_socket.accept()
print(f'Connected by {client_address}')

# menerima data dari socket client
data = client_socket.recv(1024)
print(f'Received: {data.decode()}')
# mengirim respons ke socket client
message = 'Hello, client!'
client_socket.sendall(message.encode())

# menutup koneksi
client_socket.close()
server_socket.close()