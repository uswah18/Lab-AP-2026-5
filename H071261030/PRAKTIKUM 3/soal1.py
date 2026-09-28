while True:
    item = (input("Masukkan jumlah item: "))
    try:
        jumlah_item = int(item)     
    except:
        print("input harus berupa angka!")
    
    if jumlah_item == 0:
        print("toko ditutup. sesi rekap selesai")
        break
    elif jumlah_item > 100:
        print("maksimal 100 item per transaksi!")
    elif jumlah_item < 0:
        print("jumlah tidak boleh negatif")
    else:
        print("traksaksi", item, "item berhasil!")