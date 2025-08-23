# Program Menghitung BMI (Body Mass Index)

berat = float(input("Masukan berat badan (kg): "))
tinggi = float(input("Masukan tinggi badan (m): "))

bmi = berat / (tinggi ** 2)

print(f"\nBMI anda: {bmi:.2f}")

if bmi < 18.5:
	kategori = "kurus (Underweight)"
elif 18.5 <= bmi <= 24.9:
	kategori = "Normal"
elif 25 <= bmi <= 29.9:
	if bmi >= 27 and bmi < 30:
		kategori = "Overweight (hampir obesitas)"
	else:
		kategori = "Overweight"
else:
	if bmi >= 30 and bmi < 35:
		kategori = "Obesitas kelas I"
	elif 35 >= bmi < 40:
		kategori = "Obesitas kelas II"
	else:
		kategori = "Obesitas kelas III (parah)"
		
print("kategori bmi:", kategori)

