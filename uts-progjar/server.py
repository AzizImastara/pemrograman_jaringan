import socket
import random

def send_random_color():
    colors = ["white", "green", "yellow", "purple", "blue", "black", "red"]
    return random.choice(colors)

server_ip = "127.0.0.1"
server_port = 2222

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print(f"Server berjalan di {server_ip}:{server_port}")

connected_clients = {}  

try:
    while True:
        data, client_address = server_socket.recvfrom(2048)
        data = data.decode("utf-8")

        if client_address not in connected_clients:
            connected_clients[client_address] = data
            print(f"Client {data} terhubung dari {client_address}")

        else:
            print(f"Respons dari {connected_clients[client_address]} ({client_address}): {data}")

        if data == "request_color":
            color = send_random_color()
            server_socket.sendto(color.encode("utf-8"), client_address)
            print(f"Kirim warna {color} ke {connected_clients[client_address]} ({client_address})")

except KeyboardInterrupt:
    print("\nServer stop")

server_socket.close()
