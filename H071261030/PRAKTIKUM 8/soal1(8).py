import re

def validasi_nim(nim):
    pola = r"^H071\d{6}$"
    return bool(re.match(pola, nim))

def validasi_email(email):
    pola = r"^[\w%-]+@[\w&-]+\.\w+$"
    return bool(re.match(pola, email))

def validasi_telp(telp):
    pola = r"^\d{10,13}$"
    return bool(re.match(pola, telp))

def main_validasi():
    print("=== Validasi Data Mahasiswa ===")
    nim = input("Masukkan NIM\t\t: ")
    email = input("Masukkan Email\t\t: ")
    telp = input("Masukkan No. Telp\t: ")

    status_nim = "Valid" if validasi_nim(nim) else "Format NIM tidak valid!"
    status_email = "Valid" if validasi_email(email) else "Format email tidak valid!"
    status_telp = "Valid" if validasi_telp(telp) else "Nomor telepon tidak valid!"

    print("\n--- Hasil Validasi ---")
    print(f"NIM\t\t: {status_nim}")
    print(f"Email\t\t: {status_email}")
    print(f"No. Telepon\t: {status_telp}")

    if validasi_nim(nim) and validasi_email(email) and validasi_telp(telp):
        print("\nData mahasiswa berhasil diverifikasi!")
    

main_validasi()