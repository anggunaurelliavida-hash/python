def konversi_suhu(nilai_suhu, satuan_asal, satuan_tujuan):
    
    satuan_valid = ['c', 'f', 'k']
    satuan_asal = satuan_asal.lower()
    satuan_tujuan = satuan_tujuan.lower()

    if satuan_asal not in satuan_valid or satuan_tujuan not in satuan_valid:
        return "Error: Satuan tidak valid. Masukkan hanya 'C', 'F', atau 'K'."

    
    if not isinstance(nilai_suhu, (int, float)):
        return "Error: Nilai suhu harus berupa angka."
    
    if nilai_suhu < 0 and (satuan_asal == 'k' or satuan_tujuan == 'k'):
        return "Error: Suhu Kelvin tidak boleh negatif."
    
    
    if satuan_asal == 'c':
        celsius = nilai_suhu
    elif satuan_asal == 'f':
        celsius = (nilai_suhu - 32) * 5/9
    elif satuan_asal == 'k':
        celsius = nilai_suhu - 273.15

    
    if satuan_tujuan == 'c':
        hasil = celsius
    elif satuan_tujuan == 'f':
        hasil = (celsius * 9/5) + 32
    elif satuan_tujuan == 'k':
        hasil = celsius + 273.15
    
    
    return f"Hasil: {hasil:.1f}°{satuan_tujuan.upper()}"


print("=== KONVERSI SUHU ===")
try:
    nilai = float(input("Masukkan nilai suhu: "))
    satuan_asal = input("Dari satuan (C/F/K): ")
    satuan_tujuan = input("Ke satuan (C/F/K): ")

    hasil_konversi = konversi_suhu(nilai, satuan_asal, satuan_tujuan)
    print(hasil_konversi)
except ValueError:
    print("Error: Nilai suhu harus berupa angka.")