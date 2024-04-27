import socket
import time
import threading

def translate_color(english_color):
    color_mapping = {
        "white": "putih",
        "green": "hijau",
        "yellow": "kuning",
        "purple": "ungu",
        "blue": "biru",
        "black": "hitam",
        "red": "merah",
    }
    return color_mapping.get(english_color.lower(), "tidak dikenali")

server_ip = "127.0.0.1"
server_port = 2222

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def timeout(prompt, timeout_duration):
    print(prompt, flush=True)
    response = [None]
    def input_thread():
        try:
            response[0] = input()
        except:
            pass
    thread = threading.Thread(target=input_thread)
    thread.start()
    thread.join(timeout_duration)
    if thread.is_alive():
        print(f"\nAnda tidak merespon selama {timeout_duration} detik\n")
        print("Enter untuk melanjutkan lagi\n")
        thread.join()
        return None
    else:
        return response[0]

try:
    client_name = input("Masukkan nama Anda: ")
    while True:
        client_socket.sendto(client_name.encode("utf-8"), (server_ip, server_port))
        client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))
        color, server_address = client_socket.recvfrom(2048)
        color = color.decode("utf-8")
        print(f"{color}")

        response = timeout("Sebutkan warna dalam bahasa Indonesia? ", 5)

        indonesian_color = translate_color(color)
        if response is None:
            print("Timeout \nNilai feedback: 0")
        elif response.lower() == indonesian_color:
            print("Response benar! \nNilai feedback: 100")
        else:
            print("Response salah! \nNilai feedback: 0")

        print("Silahkan tunggu 10 detik untuk menerima warna baru\n")
        time.sleep(10)
except KeyboardInterrupt:
    print("\nClient stop")

client_socket.close()
