import socket
# Inisialisasi socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Menghubungkan ke server
server_address = ('localhost', 5000)
sock.connect(server_address)
# Meminta input dari pengguna
operator = input('Masukkan operator (+, -, *, /): ')
operand1 = input('Masukkan operand pertama: ')
operand2 = input('Masukkan operand kedua: ')
# Menggabungkan operator dan operand menjadi satu string
message = operator + ' ' + operand1 + ' ' + operand2
# Mengirim pesan ke server
sock.send(message.encode())
# Menerima pesan balasan dari server
response = sock.recv(1024).decode()
print('Hasil perhitungan:', response)
# Menutup koneksi dengan server
sock.close()