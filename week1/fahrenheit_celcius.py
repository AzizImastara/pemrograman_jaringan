def fahrenheit_to_celcius(fahrenheit):
  return (fahrenheit - 32) * 5/9

def celcius_to_fahrenheit(celcius):
  return (celcius * 9/5) + 32


print("""\nPilih konversi suhu
      1. Fahrenheit
      2. Celcius""")

pilihan = int(input("Pilih konversi suhu : "))

if pilihan not in [1, 2] :
  print("Pilihan salah")
else :
  if pilihan == 1 :
    fahrenheit = float(input("Masukan suhu dalam fahrenheit: "))
    celcius = fahrenheit_to_celcius(fahrenheit)
    print("{:.2f} fahrenheit sama dengan {:.2f} celcius".format(fahrenheit, celcius))
  elif pilihan == 2 :
    celcius = float(input("Masukan suhu dalam celcius: "))
    fahrenheit = celcius_to_fahrenheit(celcius)
    print("{:.2f} celcius sama dengan {:.2f} fahrenheit".format(celcius, fahrenheit))
  else :
    print("")