print('Masukkan nilai awal dan nilai akhir')

nilai_awal = int(input(' nilai awal: '))
nilai_akhir = int(input(' nilai akhir: '))

print("\nBilangan Genap:")

for x in range(nilai_awal, nilai_akhir + 1):
    if x % 2 == 0:
        print(x, end=' ')

print('')
