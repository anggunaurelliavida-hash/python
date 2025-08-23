
harga_kopi = 18000.5
harga_roti = 10000


jumlah_kopi_int = 2
jumlah_roti_int = 3

total_harga_kopi = harga_kopi * jumlah_kopi_int
total_harga_roti = harga_roti * jumlah_roti_int

total_belanja = total_harga_kopi + total_harga_roti

# 4. Cetak hasil
print("Total harga kopi:", total_harga_kopi)
print("Total harga roti:", total_harga_roti)
print("Total belanja keseluruhan:", total_belanja)

# 5. Hitung kembalian
uang_bayar = 50000
kembalian = uang_bayar - total_belanja
print("Uang yang dibayarkan:", uang_bayar)
print("Kembalian:", kembalian)