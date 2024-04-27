import socket

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            # Request a color from the server
            client_socket.sendto(b"Request color", (server_ip, server_port))
            random_color, _ = client_socket.recvfrom(1024)
            random_color = random_color.decode()

            print(f"Received color: {random_color}")

            # Get user input for the translated color
            user_response = input("Enter the color in Bahasa Indonesia: ")

            # Validate user input
            if user_response.lower() not in ['merah', 'hijau', 'biru', 'kuning', 'ungu', 'oranye']:
                print("Invalid input! Please enter a valid color in Bahasa Indonesia.")
                continue

            # Check if the user response matches the color received from the server
            if user_response.lower() == translate_to_indonesian(random_color.lower()):
                print("Correct! You scored 100 points.")
            else:
                print("Incorrect. Try again!")

    except KeyboardInterrupt:
        print("\nClient stopped.")
    finally:
        client_socket.close()

def translate_to_indonesian(color):
    # Dictionary mapping English colors to Indonesian
    color_translations = {
        'red': 'merah',
        'green': 'hijau',
        'blue': 'biru',
        'yellow': 'kuning',
        'purple': 'ungu',
        'orange': 'oranye'
    }
    return color_translations.get(color, "unknown")

if __name__ == "__main__":
    main()
