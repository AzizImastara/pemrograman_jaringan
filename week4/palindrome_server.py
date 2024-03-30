import socket

def is_palindrome(s):
    return s == s[::-1]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)
server_socket.bind(server_address)


while True:
    print("Server is listening...")
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()
    
    if is_palindrome(message):
        response = "Palindrom"
    else:
        response = "Bukan palindrom"
        
    
    print("Menerima pesan dari client: ", message)
    server_socket.sendto(response.encode(), client_address)
