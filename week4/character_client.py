import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)

while True: 
  pesan = input("Masukkan pesan: ")

  client_socket.sendto(pesan.encode(), server_address)

  data, _ = client_socket.recvfrom(1024)
  print('Menerima balasan dari server: ', data.decode())
