import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)

while True:

  number = input("Masukkan angka: ")
  client_socket.sendto(number.encode(), server_address)

  data, server_address = client_socket.recvfrom(1024)
  print('Menerima balasan dari server: ', data.decode())

