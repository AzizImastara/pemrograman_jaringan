import socket
import random
import threading
import time

# List of colors in English and Indonesian
colors_en = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
colors_id = ['merah', 'hijau', 'biru', 'kuning', 'ungu', 'oranye']

# Function to send a random color to all clients
def send_random_color():
    while True:
        color = random.choice(colors_en)
        print(f"Sending color: {color}")
        for client in clients:
            server_socket.sendto(color.encode(), client)
        time.sleep(10)  # Wait for 10 seconds before sending next color

# Function to receive responses from clients
def receive_responses():
    while True:
        message, client_address = server_socket.recvfrom(2048)
        response = message.decode().strip().lower()
        if response in colors_id:
            print(f"Client {client_address} responded correctly with {response}")
            server_socket.sendto(b'100', client_address)  # Send 100 points to client
        else:
            print(f"Client {client_address} responded incorrectly.")
            server_socket.sendto(b'0', client_address)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

clients = set()

try:
    # Start the thread for sending random colors
    color_thread = threading.Thread(target=send_random_color)
    color_thread.daemon = True
    color_thread.start()

    # Start receiving responses from clients
    receive_responses()

except KeyboardInterrupt:
    print("Server is shutting down")
    server_socket.close()
