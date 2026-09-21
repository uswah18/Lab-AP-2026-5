# 1 Presentasi Cabai
presentasi_cabai = int(input("Masukkan presentasi cabai= "))
if presentasi_cabai >= 0 and presentasi_cabai < 11:
    print("Level Aman")
elif presentasi_cabai >= 11 and presentasi_cabai < 41:
    print("Level Sedang")
elif presentasi_cabai >= 41 and presentasi_cabai < 71:
    print("Level Pedas")
elif presentasi_cabai >= 71:
    print("Level Ekstrem")
else:
    print("Data tidak valid!")    
    
# 2 Tarif pengiriman barang
# jarak_pengiriman = int(input("Masukkan jarak pengiriman (km)= "))
# if jarak_pengiriman > 0 and jarak_pengiriman < 5: 
#     tafif_dasar = 10000
# elif jarak_pengiriman >= 5 and jarak_pengiriman < 21:
#     tarif_dasar = 20000
# elif jarak_pengiriman > 20:
#     tarif_dasar = 35000
# else:
#     print("yang bener kamu")
# express = (input("Layanan express (ya/tidak)= ")).strip().lower()
# biaya_tambahan = int(15000) if express == "ya" else int(0)

# total_tarif = tarif_dasar + biaya_tambahan
# print("Total tarif pengirim=", total_tarif )
  
# # 3 perekrutan karyawan baru
# nilai_tes = int(input("Masukkan nilai tes= "))
# pengalaman_kerja = int(input("Masukkan pengalaman kerja (tahun)= "))
# if nilai_tes >= 80:
#     print("Lolos ke Tahap Wawancara")
# elif nilai_tes < 80 and nilai_tes >= 65 and pengalaman_kerja >= 2:
#     print("Lolos Bersyarat")
# else:
#     print("Tidak lolos")    
