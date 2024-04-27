# UTS

Nama : Moh. Syahrul Aziz Imastara

NIM : 1203220084

# SOAL

Buatlah sebuah permainan yang menggunakan soket dan protokol UDP. Permainannya cukup sederhana, dengan 1 server dapat melayani banyak klien (one-to-many). Setiap 10 detik, server akan mengirimkan kata warna acak dalam bahasa Inggris kepada semua klien yang terhubung. Setiap klien harus menerima kata yang berbeda (unik). Selanjutnya, klien memiliki waktu 5 detik untuk merespons dengan kata warna dalam bahasa Indonesia. Setelah itu, server akan memberikan nilai feedback 0 jika jawabannya salah dan 100 jika benar.

# Cara Kerja Kode

Program ini menggunakan socket UDP dalam bahasa python yang menerapkan one to many yang berarti bisa melayani banyak client secara langsung

Untuk menggunakannya harus dengan mengaktifkan [server.py](https://github.com/AzizImastara/pemrograman_jaringan/blob/main/uts-progjar/server.py) terlebih dulu
dengan cara

```
python server.py
```

<img src="https://github.com/AzizImastara/pemrograman_jaringan/blob/main/uts-progjar/img/response-server.png" />

setelah server berjalan berikutnya mengaktifkan [client.py](https://github.com/AzizImastara/pemrograman_jaringan/blob/main/uts-progjar/client.py) dengan cara

```
python client.py
```

setelah mengaktifkan client akan diharuskan untuk menginputkan nama terlebih dahulu

<img src="https://github.com/AzizImastara/pemrograman_jaringan/blob/main/uts-progjar/img/client-input-nama.png" />

setelah itu client akan menerima kiriman warna dari server dan client diharuskan menjawab sebelum 5 detik

Berikut ini adalah response client jika benar menjawab :

<img src="https://github.com/AzizImastara/pemrograman_jaringan/blob/main/uts-progjar/img/jawaban-benar.png" />

Jika menjawab dengan warna yang benar maka akan dapat respon dari server berupa feedback 100

Lalu ini untuk client jika menjawab salah :

<img src="https://github.com/AzizImastara/pemrograman_jaringan/blob/main/uts-progjar/img/jawaban-salah.png" />

Jika menjawab dengan warna yang salah maka akan dapat respon dari server berupa feedback 0

Dan jika client tidak merespon dalam 5 detik :

<img src="https://github.com/AzizImastara/pemrograman_jaringan/blob/main/uts-progjar/img/tidak-meresponse.png" />

Jika tidak merespon apapun dalam 5 detik maka diharuskan untuk menekan tombol enter untuk melanjutkan program

Program ini bisa menggunakan banyak client untuk menambahkan client lagi diharuskan untuk menambahkan lagi dari cmd dan masuk folder yang anda simpan lalu ulangi cara seperti diatas

Berikut ini gambaran jika menggunakan lebih dari 1 client :

<img src="https://github.com/AzizImastara/pemrograman_jaringan/blob/main/uts-progjar/img/semua-hasil.png" />
