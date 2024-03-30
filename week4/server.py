import socket
# Inisialisasi socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind socket ke alamat dan port tertentu
server_address = ('localhost', 5000)
sock.bind(server_address)
while True:
  print('Menunggu pesan dari client...')
  data, address = sock.recvfrom(4096)

  print('Menerima pesan dari client:', data.decode())

  # Mengirim balasan ke client
  message = 'Pesan diterima oleh server!'
  sock.sendto(message.encode(), address)
