while True:
   try:
       kursi_bus = int(input("Masukkan maksimal kursi bus: "))
       if kursi_bus < 1:
           print("Input jumlah kursi dngn bnr!!") 
       else:
           break
   except:
       print("Input jumlah kursi harus berupa angka!")
       
total_pendapatan = 0
       
while kursi_bus > 0:
    print("Sisa kursi:", kursi_bus)
    input_umur = input("Masukkan umur penumpang: ")
    
    try:
        umur = int(input_umur)
    except:
        print("Input umur harus berupa angka!")
        continue
    if umur < 0:
        print("Umur tidak valid")
        continue
    
    if umur <= 5:
        kategori = "Balita"
        harga = 0
        print("Kategori:", kategori, "- Tiket Gratis")
    elif umur <= 12:
        kategori = "Anak"
        harga = 50000
        print("Kategori:", kategori, "- Harga: Rp", harga)
    else:
        kategori = "Dewasa"
        harga = 100000
        print("Kategori:", kategori, "- Harga: Rp", harga)
        
    total_pendapatan += harga
    kursi_bus -= 1
        
print("Total pendapatan perjanan PO BUS kali ini: Rp", total_pendapatan)

    
