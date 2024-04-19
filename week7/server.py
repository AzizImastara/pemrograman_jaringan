import socket
from threading import Thread

# Konfigurasi server
listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222

def kirim_pesan(handlerSocket: socket.socket):
    while True:
        message = input("server : ")
        handlerSocket.send(message.encode())

def terima_pesan(handlerSocket: socket.socket):
    while True:
        message = handlerSocket.recv(1024)
        print("client : {}".format(message.decode('utf-8')))

# Binding socket dengan IP dan port
listenerSocket.bind((serverIP, serverPort))

# Listener socket siap menerima koneksi
listenerSocket.listen(0)
print("server menunggu koneksi dari client")

# Listener socket menunggu koneksi dari client
handler, addr = listenerSocket.accept()

# Jika sudah ada koneksi dari client
print("sebuah client terkoneksi dengan alamat:{}".format(addr))

t1 = Thread(target=kirim_pesan, args=(handler,))
t2 = Thread(target=terima_pesan, args=(handler,))

t1.start()
t2.start()

t1.join()
t2.join()
