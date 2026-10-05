def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = int(subtotal * 0.9) # diskon 10%
    return subtotal


def program_kasir():
    print("Selamat datang di Kasir Minimarket!")
    status_member = input("Apakah anda member? (y/n): ").lower()
    member = (status_member == "y")

    total_pendapatan = 0
    
    while True:
        nama_barang = str(input("Masukkan nama barang (kosongkan untuk selesai): "))
        if nama_barang == "":
            break
        else:
            harga = int(input("Harga barang: "))
            jumlah = int(input("Jumlah barang: "))
            subtotal_barang = hitung_subtotal(harga, jumlah, adalah_member=member)
            print("Subtotal", nama_barang, ": Rp", subtotal_barang)
        total_pendapatan += subtotal_barang
    
    if nama_barang == "":
        print("Total belanja: Rp", total_pendapatan)
        
program_kasir()