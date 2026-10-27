import os
import random
from datetime import datetime

def siapkan_folder():
    try:
        os.makedirs("invoices", exist_ok=True)
    except IOError:
        print("Error: Gagal membuat folder invoices.")

# soal 1
def buat_invoice():
    siapkan_folder()
    
    print("\n--- MENU: BUAT TRANSAKSI BARU ---")
    nama_kasir = input("Masukkan Nama Kasir: ")
    if not nama_kasir:
        print("Nama kasir tidak boleh kosong!")
        return
        
    inisial = nama_kasir[:3].upper() if len(nama_kasir) >= 3 else nama_kasir.upper()
    
    waktu_sekarang = datetime.now()
    tahun = waktu_sekarang.strftime("%y")      
    bulan = waktu_sekarang.strftime("%m")      
    tanggal = waktu_sekarang.strftime("%d")    
    jam_menit = waktu_sekarang.strftime("%H%M") 
    
    angka_acak = str(random.randint(100, 999))
    
    id_transaksi = f"{inisial}{tahun}{bulan}{tanggal}{jam_menit}{angka_acak}"
    
    daftar_belanja = []
    total_nominal = 0
    
    while True:
        nama_produk = input("Nama Produk (ketik 'selesai' jika sudah): ")
        if nama_produk.lower() == 'selesai':
            break
        if not nama_produk:
            continue
        try:
            harga = int(input("Harga Produk: "))
            if harga < 0:
                print("Invalid")
                break
            
            jumlah = int(input("Jumlah Produk: "))
            if jumlah < 0:
                print("Invalid")
                break
            
        except ValueError:
            print("Harga dan jumlah harus berupa angka!")
            continue
            
        subtotal = harga * jumlah
        total_nominal += subtotal
        
        daftar_belanja.append({
            "nama": nama_produk,
            "harga": harga,
            "jumlah": jumlah,
            "subtotal": subtotal
        })
    
    if not daftar_belanja:
        print("Transaksi dibatalkan karena tidak ada produk yang dimasukkan.")
        return

    waktu_lengkap = waktu_sekarang.strftime('%Y-%m-%d %H:%M:%S')
    nama_file = os.path.join("invoices", f"{id_transaksi}.txt")

    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write("========================================\n") 
            file.write("             STRUK BELANJA              \n")
            file.write("========================================\n")
            file.write(f"ID Transaksi : {id_transaksi}\n")
            file.write(f"Waktu        : {waktu_lengkap}\n")
            file.write(f"Kasir        : {nama_kasir}\n")
            file.write("----------------------------------------\n")
            for item in daftar_belanja:
                file.write(f"{item['nama']} ({item['jumlah']}x) : Rp {item['subtotal']}\n")
            file.write("----------------------------------------\n")
            file.write(f"TOTAL        : Rp {total_nominal}\n")
            file.write("========================================\n")
            
        print(f"\n[SUKSES] Invoice berhasil dibuat dengan ID: {id_transaksi}")
        
        # soal 3
        catat_riwayat(waktu_lengkap, id_transaksi, total_nominal)
        
    except IOError:
        print(f"Error: Gagal menulis file invoice {nama_file}.")


# fungsi dri soal 3 (mencatat riwayat transaksi ke trx_history.txt)
def catat_riwayat(waktu, id_trx, nominal):
    file_riwayat = "trx_history.txt"
    file_sudah_ada = os.path.exists(file_riwayat)
    
    try:
        with open(file_riwayat, "a", encoding="utf-8") as file:
            if not file_sudah_ada:
                file.write("="*75 + "\n")
                file.write(f"| {'Waktu':<20} | {'ID Transaksi':<20} | {'Nominal Transaksi':<22} |\n")
                file.write("="*75 + "\n")
            
            file.write(f"| {waktu:<20} | {id_trx:<20} | Rp. {nominal:<18} |\n")
            file.write("="*75 + "\n")
    except IOError:
        print("Error: Gagal mencatat riwayat transaksi.")


# soal 2
def cari_invoice():
    print("\n--- MENU: CARI INVOICE ---")
    id_cari = input("Masukkan ID Transaksi yang dicari: ").strip()
    nama_file = os.path.join("invoices", f"{id_cari}.txt")
    
    if os.path.exists(nama_file):
        print(f"\n--- MENAMPILKAN ISI INVOICE: {id_cari} ---")
        try:
            with open(nama_file, "r", encoding="utf-8") as file:
                data = file.read() 
                print(data)
        except IOError:
            print(f"Error: Gagal membaca file {nama_file}.")
    else:
        print(f"\n[ERROR] Maaf, file invoice dengan ID '{id_cari}' tidak ditemukan di folder invoices.")

print("="*50)
print("SELAMAT DATANG".center(50))
print("="*50)

def main():
    while True:
        print("Pilih opsi:")
        print("1. Buat Transaksi Baru")
        print("2. Cari Invoice Berdasarkan ID")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ").strip()
        
        if pilihan == '1':
            buat_invoice()
        elif pilihan == '2':
            cari_invoice()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan aplikasi kasir!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


main()