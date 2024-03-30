import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)

while True: 
  message = input("Masukkan pesan: ")
  client_socket.sendto(message.encode(), server_address)

  data, server_address = client_socket.recvfrom(1024)
  print(data.decode())

