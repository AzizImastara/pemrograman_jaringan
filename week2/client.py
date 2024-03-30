import socket

# membuat objek socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# menghubungkan socket client ke server
server_address = ('localhost', 8000)
client_socket.connect(server_address)
# mengirim data ke server
message = 'Hello, server!'
client_socket.sendall(message.encode())
# menerima respons dari server
data = client_socket.recv(1024)
print(f'Received: {data.decode()}')
# menutup koneksi
client_socket.close()