import socket
import threading
def handle_client(client_socket, client_address):
  print(f"[NEW CONNECTION] Client {client_address} connected.")
  while True:
  # Menerima pesan dari client
    message = client_socket.recv(1024).decode('utf-8')
    if message == 'exit':
      break
    # Menampilkan pesan dari client
    print(f"[CLIENT {client_address}] {message}")
    # Mengirim balasan ke client
    response = input("Your response: ")
    client_socket.send(response.encode('utf-8'))
    # Menutup koneksi dengan client
  client_socket.close()
  print(f"[CONNECTION CLOSED] Client {client_address} disconnected.")
def start_server():
  # Konfigurasi host dan port
  host = '127.0.0.1'
  port = 8000
  # Membuat socket server
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((host, port))
  server_socket.listen(5)
  print("[SERVER STARTED] Waiting for connections...")
  while True:
    # Menerima koneksi dari client
    client_socket, client_address = server_socket.accept()
    # Menangani koneksi client dalam thread baru
    client_thread = threading.Thread(
    target=handle_client, args=(client_socket, client_address))
    client_thread.start()
start_server()
