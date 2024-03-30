import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)
server_socket.bind(server_address)

while True:
    print("Server is listening...")
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()
    
    character_count = len(message)
    response = "Jumlah karakter: " + str(character_count)
    
    print("Menerima pesan dari client: ", message)
    server_socket.sendto(response.encode(), client_address)
