import socket

# Fungsi untuk mengirim perintah ke server
def send_command(command):
    server_socket.send(command.encode())
    response = server_socket.recv(1024).decode()
    print(response)

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(('localhost', 12345))

print("Terhubung dengan server FTP")

while True:
    command = input("Masukkan perintah: ")

    # Kirim perintah ke server
    send_command(command)

    # Jika perintah 'byebye', tutup koneksi dan keluar dari loop
    if command == 'byebye':
        server_socket.close()
        break
