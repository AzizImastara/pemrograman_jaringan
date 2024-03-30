import socket
# Inisialisasi socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)
while True:
  message = input('Masukkan pesan: ')

  # Mengirim pesan ke server
  sock.sendto(message.encode(), server_address)

  # Menerima balasan dari server
  data, _ = sock.recvfrom(4096)
  print('Menerima balasan dari server:', data.decode())
