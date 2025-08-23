nama_pelanggan = input("masukan nama pelanggan:")

harga_kopi = 18000.5
harga_roti = 10000
jumlah_kopi_int = 2
jumlah_roti_int = 3

total_harga_kopi = harga_kopi * jumlah_kopi_int
total_harga_roti = harga_roti * jumlah_roti_int
total_belanja = total_harga_kopi + total_harga_roti

pesan_terima_kasih = "terima kasih," + nama_pelanggan + "sudah berbelanja di coffe shop bahagia!"
print("*" * 25)
print(pesan_terima_kasih)
print("*" * 25)

info_total  = "total harga kopi adalah" + str(total_belanja)
print(info_total)