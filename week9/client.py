import socket

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5000)
try:
    sock.connect(server_address)
    
    while True:
        expression = input('Masukkan operasi matematika atau ketik "exit" untuk keluar: ')
        if expression.lower() == 'exit':
            break

        sock.send(expression.encode())

        response = sock.recv(1024).decode()
        print('Hasil perhitungan:', response)
except socket.error as e:
    print(f"Terjadi kesalahan koneksi: {e}")
finally:
    sock.close()
