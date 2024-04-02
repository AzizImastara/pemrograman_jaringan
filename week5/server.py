import socket
import sys
import time
import os
import struct

print("\nWelcome to the FTP server.\n\nWaiting for client connection...\n\n")

TCP_IP = "127.0.0.1"
TCP_PORT = 1456
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

# Koneksi terhubung dengan client
print("\nConnection by address : {}".format(addr))

# Function untuk upload file
def upld():
    try:
        conn.send(b"upload")
        conn.recv(BUFFER_SIZE) 
        file_name_length = struct.unpack("h", conn.recv(2))[0]
        file_name = conn.recv(file_name_length).decode()
        conn.send(b"1")  
        file_size = struct.unpack("i", conn.recv(4))[0]
        start_time = time.time()
        print("Receiving file...")
        content = open(file_name, "wb")
        received_bytes = 0
        while received_bytes < file_size:
            l = conn.recv(BUFFER_SIZE)
            content.write(l)
            received_bytes += len(l)
        content.close()
        conn.send(b"1") 
        conn.send(struct.pack("f", time.time() - start_time)) 
        conn.send(struct.pack("i", file_size)) 
        print("File received successfully")
    except Exception as e:
        print("Error receiving file:", e)
        return

# Function untuk melihat list file
def list_files():
    print("Listing files...")
    listing = os.listdir(os.getcwd())
    conn.send(struct.pack("i", len(listing)))
    total_directory_size = 0
    for i in listing:
        conn.send(struct.pack("i", sys.getsizeof(i)))
        conn.send(i.encode())
        conn.send(struct.pack("i", os.path.getsize(i)))
        total_directory_size += os.path.getsize(i)
        conn.recv(BUFFER_SIZE)
    conn.send(struct.pack("i", total_directory_size))
    conn.recv(BUFFER_SIZE)
    print("Successfully sent file listing")
    return

# Function untuk download file
def dwld():
    conn.send(b"1")
    file_name_length = struct.unpack("h", conn.recv(2))[0]
    file_name = conn.recv(file_name_length).decode()
    if os.path.isfile(file_name):
        conn.send(struct.pack("i", os.path.getsize(file_name)))
    else:
        print("File name not valid")
        conn.send(struct.pack("i", -1))
        return
    conn.recv(BUFFER_SIZE)
    start_time = time.time()
    print("Sending file...")
    content = open(file_name, "rb")
    l = content.read(BUFFER_SIZE)
    while l:
        conn.send(l)
        l = content.read(BUFFER_SIZE)
    content.close()
    conn.recv(BUFFER_SIZE)
    conn.send(struct.pack("f", time.time() - start_time))
    print("File sent successfully")
    return

# Function untuk menghapus file
def delf():
    conn.send(b"1")
    file_name_length = struct.unpack("h", conn.recv(2))[0]
    file_name = conn.recv(file_name_length).decode()
    if os.path.isfile(file_name):
        conn.send(struct.pack("i", 1))
    else:
        conn.send(struct.pack("i", -1))
    confirm_delete = conn.recv(BUFFER_SIZE).decode()
    if confirm_delete == "Y":
        try:
            os.remove(file_name)
            conn.send(struct.pack("i", 1))
        except:
            print("Failed to delete {}".format(file_name))
            conn.send(struct.pack("i", -1))
    else:
        print("Delete abandoned by client!")
        return

# Function untuk melihat size file
def get_file_size():
    conn.send(b"1")
    file_name_length = struct.unpack("h", conn.recv(2))[0]
    file_name = conn.recv(file_name_length).decode()
    if os.path.isfile(file_name):
        conn.send(struct.pack("i", os.path.getsize(file_name)))
    else:
        conn.send(struct.pack("i", -1))
    return

# Function untuk keluar dari program
def quit():
    conn.send(b"1")
    conn.close()
    s.close()
    os.execl(sys.executable, sys.executable, *sys.argv)

while True:
    print("\n\nWaiting for instruction")
    data = conn.recv(BUFFER_SIZE).decode()
    print("\nReceived instruction: {}".format(data))
    if data == "upload":
        upld()
    elif data == "ls":
        list_files()
    elif data == "download":
        dwld()
    elif data == "rm":
        delf()
    elif data == "size":
        get_file_size()
    elif data == "byebye":
        quit()
    data = None