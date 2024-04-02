import socket
import os

# Fungsi untuk mengirim daftar file dan folder
def list_files():
    files = os.listdir('.')
    return '\n'.join(files)

# Fungsi untuk menghapus file
def remove_file(filename):
    try:
        os.remove(filename)
        return f"{filename} berhasil dihapus"
    except OSError:
        return f"Tidak dapat menghapus {filename}. File tidak ditemukan."

# Fungsi untuk mengirim file
def send_file(filename):
    try:
        with open(filename, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        return f"File {filename} tidak ditemukan."

# Fungsi untuk menerima file
def receive_file(filename, client_socket):
    with open(filename, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)
    return f"File {filename} berhasil diunggah"

# Fungsi untuk mendapatkan ukuran file
def get_file_size(filename):
    try:
        size = os.path.getsize(filename)
        return f"Ukuran file {filename}: {size / (1024 * 1024):.2f} MB"
    except FileNotFoundError:
        return f"File {filename} tidak ditemukan."

# Fungsi utama untuk menangani perintah dari client
def handle_command(command, client_socket):
    parts = command.split()
    if parts[0] == 'ls':
        return list_files()
    elif parts[0] == 'rm':
        return remove_file(parts[1])
    elif parts[0] == 'download':
        return send_file(parts[1])
    elif parts[0] == 'upload':
        return receive_file(parts[1], client_socket)
    elif parts[0] == 'size':
        return get_file_size(parts[1])
    elif parts[0] == 'byebye':
        return 'byebye'
    else:
        return 'Perintah tidak valid'

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Server FTP siap menerima koneksi...")

while True:
    # Terima koneksi dari client
    client_socket, address = server_socket.accept()
    print(f"Terhubung dengan {address}")

    while True:
        # Terima perintah dari client
        command = client_socket.recv(1024).decode()
        if not command:
            break

        # Handle perintah dari client
        response = handle_command(command, client_socket)

        # Kirim respon ke client
        client_socket.send(response.encode())

        # Jika perintah 'byebye', putus koneksi
        if response == 'byebye':
            client_socket.close()
            break
