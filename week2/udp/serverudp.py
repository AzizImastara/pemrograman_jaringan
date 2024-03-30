import socket

# Membuat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("Server is ready to receive messages.")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received message from {client_address}: {data.decode('utf-8')}")
