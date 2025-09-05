list_siswa = ['budi', 'siti', 'joko', 'ani', 'dewi']

dict_nilai_siswa = {
    'budi': 85,
    'siti': 90,
    'joko': 75,
    'ani': 88,
    'dewi':92
}

list_siswa.append('budi')
print("Daftar siswa stetlah ditambah:", list_siswa)

list('joko')
list_siswa.remove('joko')
print("Daftar siswa setelah dihapus:", list_siswa)

print("siswa pertama:", list_siswa[0])
print("siswa terakhir:", list_siswa[-1])

print("Tiga siswa terakhir:", list_siswa[-3:])

print("Daftar siswa dengsn index:")
for index, name in enumerate(list_siswa): 
    print(f"index {index}: {name}")
    
dict_nilai_siswa['ani'] = 95
print("Dictionary nilai setelah nilai ani diubah:", dict_nilai_siswa)

nilai_siti = dict_nilai_siswa.pop('siti')
print("Nilai siti yang dihgapus:", nilai_siti)
print("Dictionary nilai setlah siti dihapus:", dict_nilai_siswa)

dict_nilai_siswa['Bambang'] = dict_nilai_siswa.pop('budi')
print("Dictionary nilai setelah nama Budi diganti menjadi Bambang:", dict_nilai_siswa)