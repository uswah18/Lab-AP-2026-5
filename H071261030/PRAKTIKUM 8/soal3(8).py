import re

def bersihkan_nomor():
    print("=== Pembersihan Data Nomor Telepon ===")
    jumlah_data = int(input("Masukkan jumlah data: "))
    
    hasil_data = []
    
    for i in range(jumlah_data):
        nomor_sebelum = input(f"Nomor ke-{i+1}: ")
        nomor_sesudah = re.sub(r"[\s-]", "", nomor_sebelum) # hps spasi sm -
        
        if re.match(r"^\d{10,13}$", nomor_sesudah):
            status = "Valid"
            hasil_data.append(nomor_sesudah)
        else:
            status = "Tidak valid"
            
        hasil_data_dict = {
            "sebelum": nomor_sebelum,
            "sesudah": nomor_sesudah,
            "status": status
        }
        if i == 0:
            list_tersimpan = []
        list_tersimpan.append(hasil_data_dict)

    print("\n--- Hasil Pembersihan ---")
    for idx, data in enumerate(list_tersimpan, 1):
        print(f"Data {idx}:")
        print(f"Sebelum: {data['sebelum']}")
        print(f"Sesudah: {data['sesudah']}")
        print(f"Status : {data['status']}\n")
        
    jumlah_valid = sum(1 for d in list_tersimpan if d['status'] == "Valid")
    print(f"Jumlah nomor valid: {jumlah_valid}")
    
bersihkan_nomor() 