import socket
import threading

clients = {}

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            if message.startswith("unicast:"):
                _, recipient, msg = message.split(":", 2)
                if recipient in clients:
                    clients[recipient].send(f"Unicast from {username}: {msg}".encode())
                else:
                    client_socket.send(f"User {recipient} not found.".encode())

            elif message.startswith("multicast:"):
                _, recipients, msg = message.split(":", 2)
                recipient_list = recipients.split(",")
                for recipient in recipient_list:
                    if recipient in clients:
                        clients[recipient].send(f"Multicast from {username}: {msg}".encode())
                    else:
                        client_socket.send(f"User {recipient} not found.".encode())

            elif message.startswith("broadcast:"):
                _, msg = message.split(":", 1)
                broadcast(msg, client_socket, username)

            elif message.startswith("file:"):
                _, recipient, filename = message.split(":", 2)
                if recipient in clients:
                    clients[recipient].send(f"file:{username}:{filename}".encode())
                    threading.Thread(target=send_file, args=(client_socket, clients[recipient], filename)).start()
                else:
                    client_socket.send(f"User {recipient} not found.".encode())

            else:
                print(f"Received from {username}: {message}")
                broadcast(message, client_socket, username)

        except Exception as e:
            print(f"Error handling client {username}: {e}")
            clients.pop(username, None)
            client_socket.close()
            break

def broadcast(message, sender_socket, username):
    for client in clients.values():
        if client != sender_socket:
            try:
                client.send(f"Broadcast from {username}: {message}".encode())
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                client.close()
                clients.pop(client)

def send_file(sender_socket, recipient_socket, filename):
    try:
        with open(filename, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                recipient_socket.sendall(data)
            recipient_socket.send(b"FILE_TRANSFER_COMPLETE")
        sender_socket.send(f"File {filename} sent".encode())
    except Exception as e:
        print(f"Error sending file {filename}: {e}")
        try:
            sender_socket.send(f"Error sending file: {e}".encode())
        except:
            pass  # Handle case where sender_socket is already closed

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print("Server started on port 5555")

    while True:
        client_socket, client_address = server.accept()
        print(f"Connection from {client_address}")

        # Get the username from the client
        username = client_socket.recv(1024).decode()
        if username in clients:
            client_socket.send("Username already taken. Disconnecting.".encode())
            client_socket.close()
        else:
            clients[username] = client_socket
            client_socket.send("Welcome to the chat server!".encode())
            threading.Thread(target=handle_client, args=(client_socket, username)).start()

if __name__ == "__main__":
    start_server()
