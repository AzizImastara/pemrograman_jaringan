import socket
def start_client():
  # Konfigurasi host dan port server
  host = '127.0.0.1'
  port = 8000

  # Membuat socket client
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect((host, port))
  while True:

    # Mengirim pesan ke server
    message = input("Your message: ")
    client_socket.send(message.encode('utf-8'))
    if message == 'exit':
      break

    # Menerima balasan dari server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"[SERVER RESPONSE] {response}")
    # Menutup koneksi dengan server
  client_socket.close()
start_client()