# Tugas 2: Konversi Tipe Data dan Input Pengguna

# 1 & 2. Input dari pengguna (string)
jumlah_kopi_str = input("Masukkan jumlah pesanan kopi: ")
jumlah_roti_str = input("Masukkan jumlah pesanan roti: ")

# 3. Periksa tipe data
print("Tipe data awal jumlah kopi:", type(jumlah_kopi_str))
print("Tipe data awal jumlah roti:", type(jumlah_roti_str))

# 4. Konversi string → integer
jumlah_kopi_int = int(jumlah_kopi_str)
jumlah_roti_int = int(jumlah_roti_str)

# 5. Cek tipe data setelah konversi
print("Tipe data setelah konversi jumlah kopi:", type(jumlah_kopi_int))
print("Tipe data setelah konversi jumlah roti:", type(jumlah_roti_int)) 