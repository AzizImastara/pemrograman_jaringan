import socket
import sys
import os
import struct
import time

TCP_IP = "127.0.0.1"
TCP_PORT = 1456
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Function untuk menghubungkan socket client
def connme():
    try:
        s.connect((TCP_IP, TCP_PORT))
        print("Connection connected!")
    except:
        print("Connection failed! Make sure the server is running and the correct port is used")


# Function untuk upload file
def upld(file_name):
    try:
        s.send(b"upload")
        s.recv(BUFFER_SIZE)  
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
        file_size = os.path.getsize(file_name)
        s.send(struct.pack("i", file_size))
        start_time = time.time()
        print("Sending file...")
        content = open(file_name, "rb")
        l = content.read(BUFFER_SIZE)
        while l:
            s.send(l)
            l = content.read(BUFFER_SIZE)
        content.close()
        s.recv(BUFFER_SIZE)  
        s.send(struct.pack("f", time.time() - start_time))
        print("File sent successfully")
    except Exception as e:
        print("Error sending file:", e)
        return

# Function untuk melihat list file
def list_files():
    try:
        s.send(b"ls")
    except:
        print("Couldn't make server request. Make sure a connection has been established.")
        return
    try:
        number_of_files = struct.unpack("i", s.recv(4))[0]
        for i in range(int(number_of_files)):
            file_name_size = struct.unpack("i", s.recv(4))[0]
            file_name = s.recv(file_name_size).decode()
            file_size = struct.unpack("i", s.recv(4))[0]
            print("\t{} - {}b".format(file_name, file_size))
            s.send(b"1")
        total_directory_size = struct.unpack("i", s.recv(4))[0]
        print("Total directory size: {}b".format(total_directory_size))
    except:
        print("Couldn't retrieve listing")
        return
    try:
        s.send(b"1")
        return
    except:
        print("Couldn't get final server confirmation")
        return

# Function untuk download file
def dwld(file_name):
    try:
        s.send(b"download")
    except:
        print("Couldn't make server request. Make sure a connection has been established.")
        return
    try:
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
        file_size = struct.unpack("i", s.recv(4))[0]
        if file_size == -1:
            print("File does not exist. Make sure the name was entered correctly")
            return
    except:
        print("Error checking file")
    try:
        s.send(b"1")
        output_file = open(file_name, "wb")
        bytes_received = 0
        print("\nDownloading...")
        while bytes_received < file_size:
            l = s.recv(BUFFER_SIZE)
            output_file.write(l)
            bytes_received += BUFFER_SIZE
        output_file.close()
        print("Successfully downloaded {}".format(file_name))
        s.send(b"1")
        time_elapsed = struct.unpack("f", s.recv(4))[0]
        print("Time elapsed: {}s\nFile size: {}b".format(time_elapsed, file_size))
    except:
        print("Error downloading file")
        return
    return

# Function untuk delete file
def delf(file_name):
    try:
        s.send(b"rm")
        s.recv(BUFFER_SIZE)
    except:
        print("Couldn't connect to server. Make sure a connection has been established.")
        return
    try:
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
    except:
        print("Couldn't send file details")
        return
    try:
        file_exists = struct.unpack("i", s.recv(4))[0]
        if file_exists == -1:
            print("The file does not exist on server")
            return
    except:
        print("Couldn't determine file existence")
        return
    try:
        confirm_delete = input("Are you sure you want to delete {}? (Y/N)\n".format(file_name)).upper()
        while confirm_delete != "Y" and confirm_delete != "N" and confirm_delete != "YES" and confirm_delete != "NO":
            print("Command not recognized, try again")
            confirm_delete = input("Are you sure you want to delete {}? (Y/N)\n".format(file_name)).upper()
    except:
        print("Couldn't confirm deletion status")
        return
    try:
        if confirm_delete == "Y" or confirm_delete == "YES":
            s.send(b"Y")
            delete_status = struct.unpack("i", s.recv(4))[0]
            if delete_status == 1:
                print("File successfully deleted")
                return
            else:
                print("File failed to delete")
                return
        else:
            s.send(b"N")
            print("Delete abandoned by user!")
            return
    except:
        print("Couldn't delete file")
        return

# Function untuk cek size file
def get_file_size(file_name):
    try:
        s.send(b"size")
    except:
        print("Couldn't make server request. Make sure a connection has been established.")
        return
    try:
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
        file_size = struct.unpack("i", s.recv(4))[0]
        if file_size == -1:
            print("File does not exist. Make sure the name was entered correctly")
            return
    except:
        print("Error checking file")
    try:
        s.send(b"1")
        print("File size: {} MB".format(file_size / 1024 / 1024))
        return
    except:
        print("Couldn't get final server confirmation")
        return

# Function untuk keluar program
def quit():
    s.send(b"byebye")
    s.recv(BUFFER_SIZE)
    s.close()
    print("Server connection ended")
    return

print("Welcome to the FTP program \n")
print("connme               : Connect to server")
print("upload <file_name>   : Upload file")
print("ls                   : List file")
print("download <file_name> : Download file")
print("rm <file_name>       : Delete file")
print("size <file_name>     : Get size file")
print("byebye               : Out program")


while True:
    prompt = input("\nEnter a command: ")
    if prompt[:6].lower() == "connme":
        connme()
    elif prompt[:6].lower() == "upload":
        upld(prompt[7:])
    elif prompt.lower() == "ls":
        list_files()
    elif prompt[:8].lower() == "download":
        dwld(prompt[9:])
    elif prompt[:2].lower() == "rm":
        delf(prompt[3:])
    elif prompt[:4].lower() == "size":
        get_file_size(prompt[5:])
    elif prompt.lower() == "byebye":
        quit()
        break
    else:
        print("Command not found \n Please try again!")