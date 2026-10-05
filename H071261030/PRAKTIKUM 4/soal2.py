def hitung_statistik(*nilai):
    if len(nilai) == 0:
        return None, None, None
    nilai_rata_rata = sum(nilai) / len(nilai)
    nilai_tertinggi = max(nilai)
    nilai_terendah = min(nilai)
    return nilai_rata_rata, nilai_tertinggi, nilai_terendah

daftar_nilai = []
while True:
    nilai_ujian = (input("Masukkan nilai ujian siswa (kosongkan untuk selesai): "))
    if nilai_ujian == "":
        break
    
    if int(nilai_ujian) < 0 or int(nilai_ujian) > 100:
        print("nd bisa di nilai")
        continue
    daftar_nilai.append(float(nilai_ujian)) #

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")

rata_rata, tertinggi, terendah = hitung_statistik(*daftar_nilai)
print("Rata-rata kelas:", rata_rata)
print("Nilai tertinggi:", tertinggi)
print("Nilai terendah:", terendah)