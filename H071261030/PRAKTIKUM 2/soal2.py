# 2 Tarif pengiriman barang
jarak_pengiriman = int(input("Masukkan jarak pengiriman (km)= "))
if jarak_pengiriman > 0 and jarak_pengiriman < 5: 
    tafif_dasar = 10000
elif jarak_pengiriman >= 5 and jarak_pengiriman < 21:
    tarif_dasar = 20000
elif jarak_pengiriman > 20:
    tarif_dasar = 35000
else:
    print("yang bener kamu")
express = (input("Layanan express (ya/tidak)= ")).strip().lower()
biaya_tambahan = int(15000) if express == "ya" else int(0)

total_tarif = tarif_dasar + biaya_tambahan
print("Total tarif pengirim=", total_tarif )
  