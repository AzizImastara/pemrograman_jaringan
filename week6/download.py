import ftplib
def download_file(hostname, username, password, filename):
  try:
    # Membuat objek FTP
    ftp = ftplib.FTP(hostname)
    # Login ke server FTP
    ftp.login(username, password)
    # Ganti direktori kerja ke direktori tempat file mp4 berada
    # ftp.cwd('path/to/directory')
    # Buka file untuk ditulis
    with open(filename, 'wb') as file:
    # Unduh file mp4
      ftp.retrbinary('RETR ' + filename, file.write)
    # Tutup koneksi FTP
    ftp.quit()
    print("File berhasil diunduh.")
  except ftplib.all_errors as e:
    print("Terjadi kesalahan: ", e)

# Contoh penggunaan fungsi download_file
hostname = 'localhost'
username = 'serversyahrul'
password = '1'
filename = 'Viper_Valorant.png'

download_file(hostname, username, password, filename)