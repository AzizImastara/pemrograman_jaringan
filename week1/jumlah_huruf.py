# def hitung_jumlah_huruf(kata):
#     # Menghitung jumlah huruf dalam kata
#     jumlah_huruf = len(kata.replace(" ", ""))
    
#     return jumlah_huruf

# def main():
#     kata = input("Masukkan sebuah kata: ")
#     jumlah_huruf = hitung_jumlah_huruf(kata)
#     jumlah_kata = len(kata.split())

#     print(f"Jumlah huruf: {jumlah_huruf}")
#     print(f"Jumlah kata: {jumlah_kata}")

# if __name__ == "__main__":
#     main()

kata = input("Masukan Kata : ")
jumlah = len(kata)
print("Jumlah huruf dalam kata {} tersebut adalah {}".format(kata, jumlah))
