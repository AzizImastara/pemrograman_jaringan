# FTP Socket Programming On Python

Nama : Moh. Syahrul Aziz Imastara

NIM : 1203220084

# Soal

buat sebuah program file transfer protocol menggunakan socket programming dengan beberapa perintah dari client seperti berikut

a. ls : ketika client menginputkan command tersebut, maka server
akan memberikan daftar file dan folder

b. rm {nama file} : ketika client menginputkan command tersebut, maka server akan menghapus file dengan acuan nama file yang diberikan pada parameter pertama

c. download {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan file dengan acuan nama file yang diberikan pada parameter pertama

d. upload {nama file} : ketika client menginputkan command tersebut, maka server akan menerima dan menyimpan file dengan acuan nama file yang diberikan pada parameter pertama

e. size {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan informasi file dalam satuan MB (Mega bytes) dengan acuan nama file yang diberikan pada parameter pertama

f. byebye : ketika client menginputkan command tersebut, maka hubungan socket client akan diputus

g. connme : ketika client menginputkan command tersebut, maka hubungan socket client akan terhubung.

# Penjelasan

## server.py

Pada kode yang ada di [server.py](https://github.com/AzizImastara/pemrograman_jaringan/blob/main/week5/server.py) adalah implementasi sederhana dari sebuah FTP ( File Transfer Protocol ).
Server ini dirancang untuk berkomunikasi dengan client melalui pesan pesan teks yang mengikuti protokol yang telah ditentukan seperti :

1. upld(): Menerima file yang diunggah dari client ke server.
2. list_files(): Mengirim daftar file yang ada di direktori server ke client.
3. dwld(): Mengirim file dari server ke client.
4. delf(): Menghapus file di server.
5. get_file_size(): Mengirim ukuran file ke client.
6. quit(): Menutup koneksi dan keluar dari program.

## Alur Program

- Program berada dalam loop tak terbatas, terus menunggu intruksi dari client.
- Begitu ada instruksi yang diterima, program memprosesnya sesuai dengan fungsi yang sesuai.
- Instruksi yang didukung mencakup operasi dasar seperti upload, download, delete, dan tampilkan informasi file.

## Output

```
Welcome to the FTP server.

Waiting for client connection...
```

## client.py

Pada kode yang ada di [client.py](https://github.com/AzizImastara/pemrograman_jaringan/blob/main/week5/client.py) adalah implementasi FTP ( File Transfer Protocol ) client. Client ini memungkinkan pengguna untuk terhubung ke server FTP yang memiliki fungsi utama sebagai berikut :

1. connme(): Menghubungkan client ke server FTP.
2. upld(): Mengunggah file dari client ke server.
3. list_files(): Meminta daftar file dari server dan menampilkannya kepada pengguna.
4. dwld(): Mengunduh file dari server ke client.
5. delf(): Menghapus file dari server.
6. get_file_size(): Meminta ukuran file dari server dan menampilkannya kepada pengguna.
7. quit(): Mengakhiri koneksi dengan server dan keluar dari program.

## Alur Program

- Program menampilkan menu perintah kepada pengguna.
- Pengguna memasukkan perintah yang diinginkan.
- Program memproses perintah dan berinteraksi dengan server FTP sesuai permintaan pengguna.
- Hasil dari operasi akan ditampilkan kepada pengguna

## Output

```
Welcome to the FTP program

connme               : Connect to server
upload <file_name>   : Upload file
ls                   : List file
download <file_name> : Download file
rm <file_name>       : Delete file
size <file_name>     : Get size file
byebye               : Out program

Enter a command:
```

# Cara menggunakan

Untuk menggunakan program diharuskan menjalankan 2 file yaitu [server.py](https://github.com/AzizImastara/pemrograman_jaringan/blob/main/week5/server.py) dan [client.py](https://github.com/AzizImastara/pemrograman_jaringan/blob/main/week5/client.py)

> server.py

```

Welcome to the FTP server.

Waiting for client connection...

```

> client.py

```
Welcome to the FTP program

connme               : Connect to server
upload <file_name>   : Upload file
ls                   : List file
download <file_name> : Download file
rm <file_name>       : Delete file
size <file_name>     : Get size file
byebye               : Out program

Enter a command:
```

Di haruskan untuk menggunakan perintah connme terlebih dahulu agar client connect di server jika tidak melakukannya dipastikan tidak bisa menjalankan perintah yang lain

```
Enter a command: connme
Connection connected!
```

Setelah terhubung ke server, sekarang client dapat menggunakan perintah lainnya seperti :

1. upload (file_name)

```
Enter a command: upload file.txt
Sending file...
File sent successfully
```

Digunakan untuk upload file

2. ls

```
Enter a command: ls
        client.py - 6995b
        file.txt - 12b
        file2.txt - 3b
        le.txt - 16b
        README.md - 4776b
        server.py - 4346b
Total directory size: 16148b
```

Digunakan untuk melihat list file

3. download (file_name)

```
Enter a command: download file.txt

Downloading...
Successfully downloaded file.txt
Time elapsed: 0.0010673999786376953s
File size: 12b
```

Digunakan untuk mendownload file

4. rm (file_name)

```
Enter a command: rm file2.txt
Are you sure you want to delete file2.txt? (Y/N)
y
File successfully deleted

```

Digunakan untuk menghapus file

5. size (file_name)

```
Enter a command: size file.txt
File size: 1.1444091796875e-05 MB
```

Digunakan untuk melihat size file

6. byebye

```
Enter a command: byebye
Server connection ended
```

Digunakan untuk mengakhiri koneksi antara server dan client
