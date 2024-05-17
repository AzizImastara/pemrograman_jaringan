import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5000)
sock.bind(server_address)

sock.listen(1)
print('Menunggu koneksi dari klien...')

try:
    while True:
        client_socket, client_address = sock.accept()
        print('Terhubung dengan klien:', client_address)
        try:
            while True:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                print('Pesan diterima dari klien:', data)
                
                try:
                    result = eval(data)
                    response = str(result)
                except ZeroDivisionError:
                    response = "Error: Division by zero"
                except Exception as e:
                    response = f"Error: {str(e)}"
                
                client_socket.send(response.encode())
        except Exception as e:
            client_socket.send(f"Error: {str(e)}".encode())
        finally:
            client_socket.close()
finally:
    sock.close()
