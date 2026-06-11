#list untuk menyimpan harga tiap pesanan
total_harga = []

#procedure untuk mencetak daftar menu dan harga
def lihatmenu():
  print ("="*20, "Menu Roti", "="*20)
  print ("1. Garlic Butter      Rp 40.000,00")
  print ("2. Cheese Cake        Rp 40.000,00")
  print ("3. Almond Butter      Rp 35.000,00")
  print ("4. Brownies           Rp 30.000,00")
  print ("5. Cookies            Rp 25.000,00")

#fungsi untuk menghitung dan mengeluarkan harga per pesanan
def pesan(a):
  b = int(input("Masukkan jumlah roti yang ingin dibeli: "))
  c = int(input("Masukkan harga roti                   : "))
  d = b*c
  total_harga.append(d)
  return ("Harga pesanan roti: ", d)

#fungsi rekursif untuk menghitung jumlah harga akhir yang harus dibayarkan
def hitung_total(total_harga, i=0):
    if i == len(total_harga) - 1:
        return total_harga[i]
    else:
        return total_harga[i] + hitung_total(total_harga, i + 1)


#program utama dengan perulangan while dan percabangan if-elif-else
while True:
  print ("="*18, "Pilihan Menu", "="*18)
  print ("1. Lihat Menu Roti")
  print ("2. Pesan Roti")
  print ("3. Exit")
  pilihan = int(input("Silahkan Pilih Menu : "))
  if pilihan == 1:
    lihatmenu()
    print ()
  elif pilihan == 2:
    a = (input("Masukkan nama roti yang ingin dibeli  : "))
    print(pesan(a))
    print ()
  else:
    print ()
    print ("Total Harga:", hitung_total(total_harga))
    print ("Terima Kasih")
    break