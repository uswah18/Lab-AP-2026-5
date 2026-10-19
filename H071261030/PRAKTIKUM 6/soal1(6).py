def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {"judul": judul, "penulis": penulis, "harga": harga, "stok": stok}
    inventaris.append(buku)
    print(f"Buku {judul} berhasil ditambahkan!")
    
def cari_buku(inventaris, kata_kunci):
    hasil = [x for x in inventaris if kata_kunci.lower() in x["judul"].lower() ]
    if hasil:
        print(f"Ditemukan {len(hasil)} buku:")
        for idx, b in enumerate(hasil, 1):
            print(f"{idx}. {b['judul']}")
            print(f"{b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")
    else:
        print("Tidak ada buku yang cocok dengan kata kunci tersebut.")
    
def update_stok(inventaris, judul, jumlah):
    ditemukan = False
    for b in inventaris:
        if b["judul"].lower() == judul.lower():
            ditemukan = True
            stok_baru = b["stok"] + jumlah
            if stok_baru < 0:
                print("Gagal: Stok akhir tidak boleh negatif!")
            else:
                b["stok"] = stok_baru
                status_ubah = "berkurang" if jumlah < 0 else "bertambah"
                print(f"Stok '{b['judul']}' {status_ubah} {jumlah}. Stok sekarang: {b['stok']}")
            break
    if not ditemukan:
        print("Error: Buku tidak ditemukan dalam inventaris!")
        
def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris masih kosong.")
        return
    
    jumlah_jenis = len(inventaris)
    total_stok = sum(b["stok"] for b in inventaris)
    total_aset = sum(b["harga"] * b["stok"] for b in inventaris)
    buku_termahal = max(inventaris, key=lambda x: x["harga"])
    
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=============================")
    print(f"Jumlah jenis buku: {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print("=============================")
    print(f"Total nilai aset : Rp{total_aset}")
    print("Buku termahal")
    print(f": {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print("=============================")

def main():
    print("========================================")
    print("  SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("========================================")
    inventaris = []
    
    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            judul = input("Judul buku: ")
            penulis = input("Penulis: ")
            
            try:
                harga = float(input("Harga: "))
                stok = int(input("Stok awal: "))
                
                if harga < 0 or stok < 0:
                    print("Error: Harga dan stok tidak boleh negatif!")
                else:
                    tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Error: Harga harus berupa angka (desimal/bulat) dan stok harus berupa angka bulat!")
                
        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kata_kunci)
            
        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
                update_stok(inventaris, judul, jumlah)
            except ValueError:
                print("Error: Jumlah perubahan harus berupa angka bulat!")
                
        elif pilihan == "4":
            ringkasan_inventaris(inventaris)
            
        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1 sampai 5.")
            
main()