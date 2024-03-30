import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)
server_socket.bind(server_address)

while True:
    print("Server is listening...")
    data, client_address = server_socket.recvfrom(1024)
    numbers = list(map(int, data.decode().split()))
    
    total_sum = sum(numbers)
    response = "Hasil penjumlahan: " + str(total_sum)
    
    print("Menerima pesan dari client: ", numbers)
    server_socket.sendto(response.encode(), client_address)
