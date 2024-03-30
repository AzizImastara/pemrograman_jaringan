import socket

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)
server_socket.bind(server_address)


while True:
    print("Server is listening...")
    data, client_address = server_socket.recvfrom(1024)
    number = int(data.decode())
    
    if is_prime(number):
        response = "Bilangan prima"
    else:
        response = "Bukan bilangan prima"
    
    print("Menerima pesan dari client: ", number)
    server_socket.sendto(response.encode(), client_address)
